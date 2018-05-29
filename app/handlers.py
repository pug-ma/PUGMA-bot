from core.pugbot import PugBot
from telegram.ext import CommandHandler, Filters, MessageHandler


def start(bot, update):
    """Mostra um mensagem de apresentação do BOT."""
    message = 'Olá! Sou o Bot do Python User Group - MA (PUGMA)'
    bot.send_message(chat_id=update.message.chat_id, text=message)


def regras(bot, update):
    """Apresenta as regras do grupo."""
    message = PugBot().regras()
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
        parse_mode='Markdown'
    )


def hello_new_users(bot, update):
    """Recebe um usário novo no chat do grupo."""
    new_chat_members = update.message.new_chat_members

    for member in new_chat_members:
        is_bot = member.is_bot
        if not is_bot:
            message = (
                'Olá @{}! Seja bem vindo ao Python User Group - MA (PUG-MA). '
                'Um grupo para a galera de Python do Maranhão (ou não) que '
                'queira interagir e ficar por dentro do que está rolando na '
                'cena de Python aqui.'.format(member.username)
            )
        else:
            message = (
                '@{} 00101100 00100000 01101000 01100101 01101100 01101100 '
                '01101111 00100000 01101101 01111001 '
                '00100000 01100110 01100101 '
                '01101100 01101100 01101111 01110111 '
                '00100000 01101101 01100001 '
                '01100011 01101000 01101001 01101110 '
                '01100101 00100000 01100110 '
                '01110010 01101001 01100101 01101110'
                '01100100 00100001'.format(member.username)
            )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=PugBot().regras()
        )


def last_meetup(bot, update):
    """Apresenta o último meetup do PUG."""
    lastMeetup = PugBot().last_event()
    bot.send_photo(
        chat_id=update.message.chat_id,
        caption=lastMeetup['text'],
        photo=lastMeetup['photo']
    )


def meetup(bot, update, args):
    """
    Apresenta um meetup específico do PUG
    baseado no seu número de apresentação.
    """
    index = int(''.join(args))
    meetup = PugBot().event(index)
    bot.send_photo(
        chat_id=update.message.chat_id,
        caption=meetup['text'],
        photo=meetup['photo']
    )


start_handler = CommandHandler('start', start)
new_user_handler = MessageHandler(
    Filters.status_update.new_chat_members,
    hello_new_users
)
last_meetup_handler = CommandHandler('lastMeetup', last_meetup)
meetup_handler = CommandHandler('meetup', meetup, pass_args=True)
regras_handler = CommandHandler('regras', regras)
