import os
from decouple import Config
class Config(object):
    """
    Configuratoins of `tgEasy`.
    """
    API_ID = config("API_ID")
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
