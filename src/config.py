from contextlib import contextmanager
from dataclasses import dataclass
import json
import sqlite3


@dataclass
class Task:
    task_name: str
    frequency_days: int

    def to_sql(self):
        return


@contextmanager
def sqlite_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    cur = conn.cursor()
    yield cur
    cur.close()


def create_table() -> None:
    with sqlite3.connect("tasks.db") as conn:
        with sqlite_cursor(conn) as cur:
            cur.execute("DROP TABLE IF EXISTS tasks")
            cur.execute("CREATE TABLE tasks(task_name, frequency_days, last_done)")


def db_from_config(config_path: str, db_path: str) -> None:
    with open(config_path) as j:
        tasks = json.load(j)["tasks"]

    tasks = [(t["task_name"], t["frequency_days"], None) for t in tasks]

    with sqlite3.connect(db_path) as conn:
        with sqlite_cursor(conn) as cur:
            cur.executemany("INSERT INTO tasks VALUES(?, ?, ?)", tasks)
            conn.commit()
