import sqlite3
from datetime import date


DATABASE_NAME = "pocketwise.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(description, amount, category="Other"):
    connection = get_connection()

    today = date.today().strftime("%Y-%m-%d")

    connection.execute("""
        INSERT INTO expenses (description, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (description, amount, category, today))

    connection.commit()
    connection.close()


def get_expenses():
    connection = get_connection()

    expenses = connection.execute("""
        SELECT *
        FROM expenses
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return expenses