import database
import datetime
import peewee

class BaseModel:
  created = peewee.DateTimeField(default=datetime.datetime.now)
  updated = peewee.DateTimeField()

  def save(self, *args, **kargs):
    self.updated = datetime.datetime.now()
    return super(BaseModel, self).save(*args, **kargs)
  
  class Meta:
    database = database.db
  
