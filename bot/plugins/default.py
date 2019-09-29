"""
Ações que lidam com ChatActions ou NewMessages
que fazem matches com determinados regexes.
"""
import asyncio
import logging
from random import choices

from telethon import errors, events
from telethon.tl.custom import Button
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.utils import get_display_name, get_message_id, is_gif

from bot.configuration import settings
from bot.constants import RULES, WELCOME
from bot.utils.decorators import hidden


def default(bot):
    """
    Implementações de funcionalidades que não dependem de comandos
    digitados por um usuário.
    - arch
    - start
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
        weights = [0.1, 0.15, 0.1, 0.65]

        result = choices(population, weights)[0]

        if result is not None:
            try:
                stickers = await bot(
                    GetStickerSetRequest(
                        stickerset=InputStickerSetID(
                            id=settings.stickerset_id,
                            access_hash=settings.stickerset_hash,
                        )
                    )
                )

                msg = event.message

                await bot.send_file(
                    event.chat_id, file=stickers.documents[3], reply_to=msg.id
                )

            except errors.StickersetInvalidError as error:
                logging.error(error)

    # Mensagem de boas vindas + Regras
    @bot.on(events.ChatAction)
    async def welcome(event):
        """
        Detecta quando usuário entra no grupo (via link ou adicionado
        por outro usuário. Postando, portanto, a mensagem de boas vindas,
        seguida das regras do grupo.
        """
        last_welcome = {}

        bot_user = await bot.get_entity("me")

        conditions = [
            event.user_joined or event.user_added,
            event.user.id != bot_user.id,
        ]

        if all(conditions):
            if event.chat_id in last_welcome:
                try:
                    await last_welcome[event.chat_id].delete()
                except errors.MessageDeleteForbiddenError as error:
                    logging.error(error)

            user_id = event.user.id
            user = await bot.get_entity(user_id)

            welcome_user = (
                f'Olá <a href="tg://user?id={user_id}">{get_display_name(user)}</a>!'
            )

            await bot.send_message(
                event.chat_id,
                welcome_user + " " + WELCOME["pugma"],
                buttons=Button.url(
                    text=f"Leia as Regras do Grupo!",
                    url=f"https://t.me/{bot_user.username}?start=start",
                ),
                parse_mode="html",
            )

    @bot.on(events.NewMessage(pattern="/start", forwards=False))
    async def start(event):
        """/start: Comando que mostra a regras do grupo no PV."""
        try:
            await event.delete()
        except errors.rpcerrorlist.MessageDeleteForbiddenError as error:
            logging.error(error)

        if not (event.is_group or event.is_channel):
            message = await event.respond(RULES)
            # Sleep por 300 segundos, depois deleta a mensagem.
            await asyncio.sleep(300)
            await message.delete()
