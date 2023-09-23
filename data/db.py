from tortoise import Tortoise, run_async
from .utils import async_to_sync
from .models import Reminder


async def init():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["data.models"]})
    await Tortoise.generate_schemas()


run_async(init())


class API:
    @async_to_sync
    async def create_reminder(self, reminder: dict):
        reminder = Reminder(**reminder)
        await reminder.save()

    @async_to_sync
    async def get_reminders(self):
        datas = [{"title": reminder.title, "text": reminder.text} async for reminder in Reminder.all()]
        return datas
