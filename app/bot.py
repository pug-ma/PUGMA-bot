from decouple import config
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from core.pugbot import PugBot

API_KEY = config('TOKEN')
APP_NAME = config('APP_NAME')
PORT = int(config('PORT', default='8443'))


def start(bot, update):
    message = 'Olá! Sou o Bot do Python User Group - MA (PUGMA)'
    bot.send_message(chat_id=update.message.chat_id, text=message)


def hello_new_users(bot, update):
    """Recebe um usário novo no chat do grupo"""
    new_chat_members = update.message.new_chat_members

    for member in new_chat_members:
        is_bot = member.is_bot
        if not is_bot:
            message = ('Olá @{}! Seja bem vindo ao Python User Group - MA (PUG-MA). '
                       'Um grupo para a galera de Python do Maranhão (ou não) que '
                       'queira interagir e ficar por dentro do que está rolando na '
                       'cena de Python aqui.'.format(member.username)
                       )
        else:
            message = ('@{} 00101100 00100000 01101000 01100101 01101100 01101100 '
                       '01101111 00100000 01101101 01111001 00100000 01100110 01100101 '
                       '01101100 01101100 01101111 01110111 00100000 01101101 01100001 '
                       '01100011 01101000 01101001 01101110 01100101 00100000 01100110 '
                       '01110010 01101001 01100101 01101110'
                       '01100100 00100001'.format(member.username)
                       )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=message
        )


def last_meetup(bot, update):
    lastMeetup = PugBot().lastEvent()
    bot.send_photo(
        chat_id=update.message.chat_id,
        caption=lastMeetup['text'],
        photo=lastMeetup['photo']
    )


def meetup(bot, update, args):
    index = int(''.join(args))
    meetup = PugBot().Event(index)
    bot.send_photo(
        chat_id=update.message.chat_id,
        caption=meetup['text'],
        photo=meetup['photo']
    )


def main():
    updater = Updater(token=API_KEY)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    new_user_handler = MessageHandler(
        Filters.status_update.new_chat_members,
        hello_new_users
    )
    last_meetup_handler = CommandHandler('lastMeetup', last_meetup)
    meetup_handler = CommandHandler('meetup', meetup, pass_args=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(new_user_handler)
    dispatcher.add_handler(meetup_handler)
    dispatcher.add_handler(last_meetup_handler)

    # updater.start_webhook(listen='0.0.0.0',
    #                      port=PORT,
    #                      url_path=API_KEY)
    #updater.bot.set_webhook(str(APP_NAME) + '/' + str(API_KEY))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
