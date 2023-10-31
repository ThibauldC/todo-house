from config import db_from_config
from repository import get_tasks, create_task_table

if __name__ == '__main__':
    create_task_table()
    db_from_config("conf/tasks.json")
    print(get_tasks("tasks.db"))

