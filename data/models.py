from typing import Any
from tortoise.models import Model
from tortoise import fields

class Reminder(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=26, null=False, blank=False)
    text = fields.TextField(null=False, blank=False)
    importance = fields.CharField(max_length=26, null=False, blank=False, default="Hi")
    created_at = fields.DatetimeField(auto_now_add=True)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        # constraint importance must be one of ("Hi", "Normal")
        assert self.importance in ("Hi", "Normal", "Low")