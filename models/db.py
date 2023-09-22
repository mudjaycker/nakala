from tortoise import Tortoise, run_async
from utils import async_to_sync
from tables import Reminder

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

run_async(init())

@async_to_sync
async def create_reminder(reminder:dict):
    reminder = Reminder(**reminder)
    await reminder.save()

@async_to_sync
async def get_reminders():...