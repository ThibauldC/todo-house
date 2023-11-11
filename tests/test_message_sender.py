from datetime import datetime
from unittest.mock import patch

from freezegun import freeze_time

from src.message_sender import format_message_to_markdown
from src.models import Task


@freeze_time("2023-11-07")
def test_format_markdown():
    tasks = [
        Task("task_1", 1, datetime.today()),
        Task("task_2", 2, datetime.today()),
        Task("task_3", 3, datetime.today())
    ]

    expected_header = f"*TO DO ON 07/11/2023*:\n\n"
    expected_message = "\n".join(["\- task_1", "\- task_2", "\- task_3"])

    assert format_message_to_markdown(tasks) == expected_header + expected_message


# @patch("message_sender.Bot")
# def test_send_message(mock_bot):
#     mock_bot.send_message.assert_called_once()
