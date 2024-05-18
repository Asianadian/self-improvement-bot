import enum
import peewee

from users.models import User
from base.models import BaseModel

class PointType(enum.Enum):
  TEMP = {'points': 1, 'id': 'TEMP_POINT'}


class UserActivity(BaseModel):
  user_id = peewee.ForeignKeyField(model=User)
  reason = peewee.CharField(max_length=100)
  delta = peewee.FloatField()