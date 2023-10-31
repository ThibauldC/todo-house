from config import db_from_config, create_table

if __name__ == '__main__':
    create_table()
    db_from_config("conf/tasks.json", "tasks.db")

