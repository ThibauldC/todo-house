from datetime import datetime
import os

from telegram import Bot
from telegram.constants import ParseMode

from src.models import Task

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


async def send_message(message: str):
    bot = Bot(BOT_TOKEN)

    async with bot:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode=ParseMode.MARKDOWN_V2
        )


def format_message_to_markdown(tasks_to_do: list[Task]) -> str:
    header = f"*TO DO ON {datetime.today().date().strftime('%d/%m/%Y')}*:\n\n"
    task_list = "\n".join([f"\- {task.task_name}" for task in tasks_to_do])
    return header + task_list

