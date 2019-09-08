"""
Pra extender o bot basta criar uma função que recebe como argumento
um TelegramClient:

* Vide __init__.py
* https://docs.telethon.dev/en/latest/quick-references/client-reference

Exemplo:
def <closure>(bot):
    @bot.on(<args>):
    async def <func_name>(<event>):
        <implementação>

Ao adicionar um novo comando, tente mantê-los em ordem alfabética
dentro da closure e da documentação:

    async def f1(<event>):
        (...)

    async def g2(<event>):
        (...)

    async def h3(<event>):
        (...)
"""

import asyncio
from itertools import repeat
from operator import eq
from random import choices

import requests
from PIL import Image
from telethon import errors, events
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID

from .configuration import github_data, settings
from .constants import RULES, SPAM, WELCOME
from .utils import hidden, photo_meetup


def default(bot):
    """
    Implementações de funcionalidades que não dependem de comandos
    digitados por um usuário.
    - arch
    - welcome
    """

    # Exemplo de como enviar stickers e ocultar commandos
    @bot.on(events.NewMessage(pattern=r"(?i).*(babaca|babaquice|arch)"))
    @hidden
    async def arch(event):
        """
        Envia o sticker do babaca quando ocorre um match com o regex. É
        escondido da saída do '/help' através do decorator @hidden.
        """
        population = ["arch", "babaca", "babaquice", None]
        weights = [0.05, 0.08, 0.07, 0.8]

        result = choices(population, weights)[0]

        if result is not None:
            stickers = await bot(
                GetStickerSetRequest(
                    stickerset=InputStickerSetID(
                        id=settings.stickerset_id, access_hash=settings.stickerset_hash
                    )
                )
            )

            msg = event.message

            await bot.send_file(
                event.chat_id, file=stickers.documents[3], reply_to=msg.id
            )

    # Mensagem de boas vindas + Regras
    @bot.on(events.ChatAction)
    async def welcome(event):
        """
        Detecta quando usuário entra no grupo (via link ou adicionado
        por outro usuário. Postando, portanto, a mensagem de boas vindas,
        seguida das regras do grupo.
        """
        last_welcome = {}
        if event.user_joined or event.user_added:
            if event.chat_id in last_welcome:
                try:
                    await last_welcome[event.chat_id].delete()
                except errors.MessageDeleteForbiddenError:
                    pass

            last_welcome[event.chat_id] = await event.reply(WELCOME["pugma"])
            await bot.send_message(event.chat_id, RULES)


def commands(bot):
    """
    Implementações de comandos básicos:
    - /help
    - /meetup <d:int>?
    - /spam(mer)
    - /version
    """

    @bot.on(events.NewMessage(pattern="/help", forwards=False))
    async def help(event):
        """/help: Lista todos os comandos implementados."""
        await event.delete()

        text = "Lista de comandos:\n"

        # Altenartiva para evitar escrever
        # um condicional gigante
        conditions = lambda x, y: [
            isinstance(x, events.NewMessage),
            y.__doc__ is not None,
            not hasattr(y, "is_hidden"),
        ]

        for callback, handler in bot.list_event_handlers():
            if all(map(eq, conditions(handler, callback), repeat(True))):
                text += f"- {callback.__doc__.strip()}\n"

        message = await event.respond(text, link_preview=False)
        # Sleep por 40 segundos, depois deleta a mensagem.
        await asyncio.sleep(40)
        await message.delete()

    @bot.on(events.NewMessage(pattern="/meetup(\s{1,5}\d{0,2})?", forwards=False))
    async def meetup(event):
        """/meetup: Consulta a API do Github e manda o último meetup."""

        message = event.pattern_match.group()
        matches = message.split(" ")

        await event.delete()

        photo_url, event_num = photo_meetup(github_data, matches)

        if photo_url and event_num:
            text = "Meetup PUG-MA: " + str(event_num)
            await bot.send_file(event.chat_id, file=photo_url, caption=text)

    @bot.on(events.NewMessage(pattern="/spam(mer)?", forwards=False))
    async def spam(event):
        """/spam, #spammer: Informa que spam não é bem vindo no grupo, seguido da deleção da mensagem."""
        await asyncio.wait(
            [event.delete(), event.respond(SPAM, reply_to=event.reply_to_msg_id)]
        )

    @bot.on(events.NewMessage(pattern="/version", forwards=False))
    async def version(event):
        """/version: Versão atual e repositório do Bot."""
        await event.delete()

        text = f"**Bot do Python User Group - MA**"

        text += (
            "\n\nVocê pode contribuir com o desenvolvimento do bot "
            "via **PRs** **Issues**, ou **Code Reviews** no "
            "[nosso repositório](https://github.com/pug-ma/PUGMA-BOT)."
        )

        await event.respond(text, link_preview=True)
