import peewee

from base.models import BaseModel

class User(BaseModel):
  user_id = peewee.CharField(max_length=100)
  total_points = peewee.FloatField()
  