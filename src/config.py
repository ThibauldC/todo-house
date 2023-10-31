import json

from src.repository import insert_tasks


def db_from_config(config_path: str) -> None:
    with open(config_path) as j:
        tasks = json.load(j)["tasks"]

    tasks = [(t["task_name"], t["frequency_days"], None) for t in tasks]

    insert_tasks("tasks.db", tasks)
