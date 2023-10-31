from datetime import datetime
import sqlite3

from src.connection import sqlite_cursor
from src.models import Task


# TODO: get db_path from config_file?
def get_tasks(db_path: str) -> list[Task]:
    with sqlite3.connect(db_path) as conn:
        with sqlite_cursor(conn) as cur:
            cur.execute("SELECT * FROM tasks")
            tasks = [Task(*t) for t in cur.fetchall()]
    return tasks


def insert_tasks(db_path: str, tasks: list[tuple[str, int, None]]) -> None:
    with sqlite3.connect(db_path) as conn:
        with sqlite_cursor(conn) as cur:
            cur.executemany("INSERT INTO tasks VALUES(?, ?, ?)", tasks)
            conn.commit()


def update_tasks(db_path: str, updated_tasks: list[tuple[str, datetime.date]]) -> None:
    with sqlite3.connect(db_path) as conn:
        with sqlite_cursor(conn) as cur:
            cur.executemany(
                """
                UPDATE tasks
                SET last_done = ?
                WHERE task_name = ?
                """
                , updated_tasks
            )
            conn.commit()


def create_task_table() -> None:
    with sqlite3.connect("tasks.db") as conn:
        with sqlite_cursor(conn) as cur:
            cur.execute("DROP TABLE IF EXISTS tasks")
            cur.execute("CREATE TABLE tasks(task_name, frequency_days, last_done)")
