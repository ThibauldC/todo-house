import asyncio

from service import db_from_config, get_tasks_to_do, update_tasks_done
from message_sender import send_message, format_message_to_markdown

if __name__ == '__main__':
    db_from_config("conf/tasks.json")
    tasks_to_do = get_tasks_to_do("tasks.db")
    mess = format_message_to_markdown(tasks_to_do)
    asyncio.run(send_message(mess))
    update_tasks_done("tasks.db", tasks_to_do)

