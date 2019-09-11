"""
Para gerar sua string session a fim de
debug. Basta colocar o token do seu
bot quando for pedido.
"""

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from bot import settings

with TelegramClient(StringSession(), settings.api_id, settings.api_hash) as client:
    print(client.session.save())
