"""
Ações que lidam com ChatActions ou NewMessages
que fazem matches com determinados regexes.
"""

import logging
from random import choices

from telethon import errors, events
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID

from bot.configuration import settings
from bot.constants import RULES, WELCOME
from bot.utils.decorators import hidden


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

        bot_id = await bot.get_peer_id("me")

        conditions = [event.user_joined or event.user_added, event.user.id != bot_id]

        if all(conditions):
            if event.chat_id in last_welcome:
                try:
                    await last_welcome[event.chat_id].delete()
                except errors.MessageDeleteForbiddenError as error:
                    logging.error(error)

            last_welcome[event.chat_id] = await event.reply(WELCOME["pugma"])
            await bot.send_message(event.chat_id, RULES)
