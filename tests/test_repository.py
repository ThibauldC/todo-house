import os
import sqlite3
import tempfile

import pytest

from src.repository import create_task_table


@pytest.fixture
def sqlite_db() -> str:
    with tempfile.TemporaryDirectory() as temp_dir:
        db_location = f"{temp_dir}/test.db"
        yield db_location


def test_create_task_table(sqlite_db):
    create_task_table(sqlite_db)

    assert os.path.exists(sqlite_db)
    with sqlite3.connect(sqlite_db) as conn:
        cursor = conn.cursor()
        tables = [table[0] for table in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        cursor.close()

    assert "tasks" in tables
