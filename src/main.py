from service import db_from_config, get_tasks_to_do, update_tasks_done

if __name__ == '__main__':
    # db_from_config("conf/tasks.json")
    tasks_to_do = get_tasks_to_do("tasks.db")
    print(tasks_to_do)
    # create Telegram message and send to channel
    update_tasks_done("tasks.db", tasks_to_do)


