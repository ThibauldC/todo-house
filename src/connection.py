from contextlib import contextmanager
import sqlite3


@contextmanager
def sqlite_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    cur = conn.cursor()
    yield cur
    cur.close()
