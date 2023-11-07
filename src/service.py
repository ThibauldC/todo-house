from datetime import datetime, timedelta
import json

from src.models import Task
from src.repository import insert_tasks, create_task_table, get_tasks, update_tasks


def db_from_config(config_path: str) -> None:
    # TODO: create an option to fully drop table and re-insert everything + option to just add new tasks
    create_task_table()
    with open(config_path) as j:
        tasks = json.load(j)["tasks"]

    tasks = [(t["task_name"], t["frequency_days"], datetime.today().date() - timedelta(days=1)) for t in tasks]

    insert_tasks("tasks.db", tasks)


def get_tasks_to_do(db_path: str) -> list[Task]:
    tasks = get_tasks(db_path)
    tasks_to_do = [
        task for task in tasks
        if (task.last_done + timedelta(days=task.frequency_days)).date() == datetime.today().date()
           or (task.last_done + timedelta(days=task.frequency_days)).date() < datetime.today().date()
    ]
    return tasks_to_do


def update_tasks_done(db_path: str, tasks_done: list[Task]) -> None:
    last_done = datetime.today().date()
    tasks_to_update = [(last_done, task.task_name) for task in tasks_done]
    update_tasks(db_path, tasks_to_update)
