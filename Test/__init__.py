"""
✓ KayAspirerProject 2021
"""

from telethon import TelegramClient
from decouple import config
import logging
import time
from Test.config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

"""
#Normal Usage

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
"""

app = TelegramClient('app', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
