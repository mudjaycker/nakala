from tortoise.models import Model
from tortoise import fields

class Reminder(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=26, null=False, blank=False)
    text = fields.TextField(null=False, blank=False)
    created_at = fields.DatetimeField(auto_now_add=True)