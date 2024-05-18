import logging

from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

def get_formatted_logger():
  default_formatter = Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S"
  )

  default_handler = TimedRotatingFileHandler(
    filename='./logs/discord.log', 
    when='D', 
    interval=1, 
    backupCount=1, 
    encoding='utf-8', 
    delay=False,
  )
  
  default_handler.setFormatter(default_formatter)
  
  logging.basicConfig(level=logging.DEBUG)
  logging.getLogger().handlers.clear()
  logging.getLogger().addHandler(default_handler)
  
  return logging