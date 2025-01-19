from .init_db import *
from .utils import async_to_sync, T_Todo
from .models import Reminder


class API:
    def __init__(self):
        print("API initialized")

    @async_to_sync
    async def create(self, data: T_Todo):
        reminder = Reminder(**data)
        await reminder.save()
        return None

    @async_to_sync
    async def get(self):
        datas: list[T_Todo] = [
            {
                "title": todo.title,
                "importance": todo.importance,
                "text": todo.text,
                "date": todo.created_at.isoformat(),
            }
            async for todo in Reminder.all()
        ]
        return datas
