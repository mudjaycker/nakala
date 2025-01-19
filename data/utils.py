import asyncio
from typing import Callable
from tortoise import fields
import typing as t


T_ = t.TypeVar("T_")
P_ = t.ParamSpec("P_")
U_ = t.TypeVar("U_")


def async_to_sync(
    func: Callable[P_, t.Coroutine[T_, t.Any, t.Any]]
) -> t.Callable[P_, T_]:

    def inner(*args: P_.args, **kwargs: P_.kwargs):

        async def create_task(*args: P_.args, **kwargs: P_.kwargs):
            return await asyncio.create_task(func(*args, **kwargs))

        return asyncio.run(create_task(*args, **kwargs))

    return inner


class IntChoice(fields.IntField):
    calledTime: int = 0
    choices: t.Iterable[int] = []

    def __init__(self, primary_key: bool | None = None, **kwargs: dict[str, t.Any]):
        super().__init__(primary_key, **kwargs)

    def validate(self, value: t.Any):
        if value not in self.choices and IntChoice.calledTime > 1:
            raise LookupError("Not in choices")

        IntChoice.calledTime += 1
        return super().validate(value)


class T_Todo(t.TypedDict):
    title: str
    importance: int
    text: str
    date: t.Optional[str]