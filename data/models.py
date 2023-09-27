from typing import Any
from tortoise.models import Model
from tortoise import fields


class Reminder(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=26, null=False, blank=False)
    text = fields.TextField(null=False, blank=False)
    importance = fields.IntField(max_length=26, null=False, blank=False, default=0)
    created_at = fields.DatetimeField(auto_now_add=True)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.importances = ["Low", "Normal", "High"]
        # print(f"====> {type(self.importance)}")
        # constraint importance must be one of ("Hi", "Normal", "Low")
        # assert self.importance in [self.importances.index(i) for i in self.importances]

    def __str__(self) -> str:
        return f"{self.title=} {self.importances[self.importance]=} {self.created_at=}"
