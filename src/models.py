from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    task_name: str
    frequency_days: int
    last_done: Optional[datetime.date]
