from tortoise.models import Model
from tortoise import fields
from .utils import IntChoice


class Importance(IntChoice):
    choices = tuple(range(3))


class Reminder(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=26, null=False, blank=False)
    text = fields.TextField(null=False, blank=False)
    importance = Importance(max_length=26, null=False, blank=False, default=0)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title=} {self.importance=} {self.created_at=}"
