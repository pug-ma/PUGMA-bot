"""
Comandos usados por um usuário comuns sem permissões de administrador.
"""

import asyncio
from itertools import repeat
from operator import eq

from telethon import errors, events

from bot.configuration.github import GithubData
from bot.constants import SPAM
from bot.utils.github import photo_meetup

github_data = GithubData()


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
        """/spam, /spammer: Informa que spam não é bem vindo no grupo, seguido da deleção da mensagem."""
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
