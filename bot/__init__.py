import asyncio
import logging
import sys
from itertools import repeat
from operator import eq

from telethon import TelegramClient, errors, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID

from .configuration import settings
from .core import commands, default

logging_level = logging.INFO if settings.debug else logging.WARNING

logging.basicConfig(
    stream=sys.stdout,
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging_level,
)

async_logger = logging.getLogger("asyncio")
async_logger.setLevel(logging.ERROR)

SESSION = settings.session

bot = TelegramClient(StringSession(SESSION), settings.api_id, settings.api_hash)

# Setando os handlers do bot
default(bot)
commands(bot)
