from tortoise.models import Model
from tortoise import fields

class Reminder(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=26)
    text = fields.TextField()