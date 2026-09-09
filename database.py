import sqlite3
from contextlib import closing
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "faults.db"

def initialise_database():
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS faults (
                    id INTEGER PRIMARY KEY,
                    equipment TEXT NOT NULL,
                    description TEXT NOT NULL,
                    priority TEXT NOT NULL
                        CHECK (priority IN ('low', 'medium', 'high')),
                    status TEXT NOT NULL DEFAULT 'open',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)

def save_fault(equipment, description, priority):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            cursor = connection.execute("""
                INSERT INTO faults (equipment, description, priority)
                VALUES (?, ?, ?)
            """, (equipment, description, priority))

            return cursor.lastrowid