
from flask import Flask, render_template, request, redirect, url_for
from database import get_connection, init_db

app = Flask(__name__)

# Create the database table if it doesn't exist.
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    rider = request.form.get("rider", "").strip()
    bike_type = request.form.get("bike_type", "")
    problem = request.form.get("problem", "").strip()
    preferred_day = request.form.get("preferred_day", "").strip()

    # Check the form information.
    if not rider:
        return "Rider label is required.", 400

    if bike_type not in ("city", "road", "other"):
        return "Invalid bike type.", 400

    if not 1 <= len(problem) <= 240:
        return "Problem must be 1–240 characters.", 400

    if len(preferred_day) > 40:
        return "Preferred day is too long.", 400

    # Save the inquiry.
    connection = get_connection()
    cursor = connection.execute(
        """
        INSERT INTO repairs
        (rider, bike_type, problem, preferred_day, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (rider, bike_type, problem, preferred_day, "Pending review"),
    )
    connection.commit()
    inquiry_id = cursor.lastrowid
    connection.close()

    return (
        f"Repair inquiry #{inquiry_id} saved! "
        "Status: Pending review. "
        "This is not an appointment confirmation."
    )



@app.route("/queue")
def queue():
    connection = get_connection()

    repairs = connection.execute(
        "SELECT * FROM repairs ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template("queue.html", repairs=repairs)


@app.route("/repair/<int:repair_id>")
def repair_detail(repair_id):
    connection = get_connection()

    repair = connection.execute(
        "SELECT * FROM repairs WHERE id = ?",
        (repair_id,)
    ).fetchone()

    connection.close()

    if repair is None:
        return "Repair inquiry not found.", 404

    return render_template("detail.html", repair=repair)


@app.route("/repair/<int:repair_id>/status", methods=["POST"])
def update_status(repair_id):
    new_status = request.form.get("status", "")

    allowed_transitions = {
        "Pending review": {"Accepted", "Declined"},
        "Accepted": {"Completed"},
        "Declined": set(),
        "Completed": set(),
    }

    connection = get_connection()

    repair = connection.execute(
        "SELECT * FROM repairs WHERE id = ?",
        (repair_id,)
    ).fetchone()

    if repair is None:
        connection.close()
        return "Repair inquiry not found.", 404

    current_status = repair["status"]

    if new_status not in allowed_transitions.get(current_status, set()):
        connection.close()
        return "Invalid status change.", 400

    connection.execute(
        "UPDATE repairs SET status = ? WHERE id = ?",
        (new_status, repair_id)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("repair_detail", repair_id=repair_id))

if __name__ == "__main__":
    app.run(debug=True)
