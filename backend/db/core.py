import os
import sqlite3 as sql
from environment.variables import DATABASE

from typing import Tuple

module_path = os.path.dirname(__file__)
db_path = os.path.join(module_path, DATABASE)
test_db_path = os.path.join(module_path, "test.db")


def connect() -> Tuple[sql.Cursor, sql.Connection]:
    connection = sql.connect(db_path)
    cursor = connection.cursor()
    return cursor, connection


def create_user_table() -> None:
    cursor, connection = connect()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            ssn TEXT NOT NULL
    );"""
    )
    connection.commit()
    connection.close()


def show_tables() -> None:
    cursor, connection = connect()
    response = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    for table in response.fetchall():
        print(table)
    connection.commit()
    connection.close()


def clear_table(table_name: str) -> None:
    cursor, connection = connect()
    cursor.execute(f"DELETE FROM {table_name}")
    connection.commit()
    connection.close()


def drop_table(table_name: str) -> None:
    cursor, connection = connect()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    connection.commit()
    connection.close()
