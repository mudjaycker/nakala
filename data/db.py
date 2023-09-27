from .init_db import *
from .utils import async_to_sync
from .models import Reminder


class API:
    @async_to_sync
    async def create(self, reminder):
        reminder = Reminder(**reminder)
        await reminder.save()

    @async_to_sync
    async def get(self):
        datas = [
            {
                "title": reminder.title,
                "text": reminder.text,
                "importance": reminder.importances[reminder.importance],
                "date": reminder.created_at,
            }
            async for reminder in Reminder.all()
        ]
        return datas


# api = API()
# r = Reminder(title="test", text="test", importance=1)
# print(r)
# print(api.get())
