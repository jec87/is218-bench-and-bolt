
import sqlite3

DATABASE = "repairs.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS repairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rider TEXT NOT NULL,
            bike_type TEXT NOT NULL,
            problem TEXT NOT NULL,
            preferred_day TEXT,
            status TEXT NOT NULL DEFAULT 'Pending review'
        )
    """)

    connection.commit()
    connection.close()
