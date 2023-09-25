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
        datas = [{"title": reminder.title, "text": reminder.text} async for reminder in Reminder.all()]
        return datas
