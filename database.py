import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        event_type TEXT NOT NULL,
        guests INTEGER,
        budget INTEGER,
        event_date TEXT,
        requirements TEXT,
        priority TEXT,
        package_name TEXT,
        ai_message TEXT,
        status TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_lead(
    name,
    phone,
    email,
    event_type,
    guests,
    budget,
    event_date,
    requirements,
    priority,
    package_name,
    ai_message,
    status
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads(
        name,
        phone,
        email,
        event_type,
        guests,
        budget,
        event_date,
        requirements,
        priority,
        package_name,
        ai_message,
        status
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        name,
        phone,
        email,
        event_type,
        guests,
        budget,
        event_date,
        requirements,
        priority,
        package_name,
        ai_message,
        status
    ))

    conn.commit()
    conn.close()


def get_all_leads():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM leads
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_lead(lead_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM leads WHERE id=?",
        (lead_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


def update_status(lead_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE leads
        SET status=?
        WHERE id=?
        """,
        (status, lead_id)
    )

    conn.commit()
    conn.close()


def delete_lead(lead_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM leads WHERE id=?",
        (lead_id,)
    )

    conn.commit()
    conn.close()