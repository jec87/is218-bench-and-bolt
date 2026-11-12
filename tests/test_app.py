
import pytest

from app import app
from database import init_db, get_connection


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_database = tmp_path / "test_repairs.db"

    import database
    monkeypatch.setattr(database, "DATABASE", str(test_database))

    init_db()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bench & Bolt" in response.data


def test_valid_repair_request(client):
    response = client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "city",
        "problem": "Front brake is squeaking",
        "preferred_day": "Friday"
    })

    assert response.status_code == 200
    assert b"Pending review" in response.data

    connection = get_connection()
    repair = connection.execute(
        "SELECT * FROM repairs"
    ).fetchone()
    connection.close()

    assert repair["rider"] == "Test Rider"
    assert repair["status"] == "Pending review"


def test_blank_problem_is_rejected(client):
    response = client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "city",
        "problem": "",
        "preferred_day": ""
    })

    assert response.status_code == 400


def test_invalid_bike_type_is_rejected(client):
    response = client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "motorcycle",
        "problem": "Broken wheel",
        "preferred_day": ""
    })

    assert response.status_code == 400


def test_overlong_problem_is_rejected(client):
    response = client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "city",
        "problem": "A" * 241,
        "preferred_day": ""
    })

    assert response.status_code == 400


def test_status_changes(client):
    client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "city",
        "problem": "Flat tire",
        "preferred_day": ""
    })

    response = client.post(
        "/repair/1/status",
        data={"status": "Accepted"}
    )
    assert response.status_code == 302

    response = client.post(
        "/repair/1/status",
        data={"status": "Completed"}
    )
    assert response.status_code == 302


def test_pending_cannot_be_completed(client):
    client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "city",
        "problem": "Flat tire",
        "preferred_day": ""
    })

    response = client.post(
        "/repair/1/status",
        data={"status": "Completed"}
    )

    assert response.status_code == 400


def test_declined_cannot_be_reopened(client):
    client.post("/submit", data={
        "rider": "Test Rider",
        "bike_type": "road",
        "problem": "Broken chain",
        "preferred_day": ""
    })

    client.post(
        "/repair/1/status",
        data={"status": "Declined"}
    )

    response = client.post(
        "/repair/1/status",
        data={"status": "Accepted"}
    )

    assert response.status_code == 400
