from tortoise import Tortoise, run_async  # type: ignore


async def init():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["data.models"]})  # type: ignore
    await Tortoise.generate_schemas()


run_async(init())
