import asyncio
import logging
import sys

from telethon import TelegramClient, errors, events
from telethon.sessions import StringSession

from .configuration import settings
from .plugins.default import default
from .plugins.user import commands

LOGGING_LEVEL = logging.INFO if settings.debug else logging.WARNING

logging.basicConfig(
    stream=sys.stdout,
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=LOGGING_LEVEL,
)

async_logger = logging.getLogger("asyncio")
async_logger.setLevel(logging.ERROR)

SESSION = settings.session

Bot = TelegramClient(StringSession(SESSION), settings.api_id, settings.api_hash)

SPAMMERS = {}

# Setando os handlers do bot
default(Bot)
commands(Bot)
