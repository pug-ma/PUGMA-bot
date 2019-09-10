"""
Para gerar sua string session a fim de
debug. Basta colocar o token do seu
bot quando for pedido.
"""

from bot import bot, settings

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), settings.api_id, settings.api_hash) as client:
    print(client.session.save())
