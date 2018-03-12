import telegram
from telegram.ext import (
    Updater, 
    MessageHandler, 
    Filters,
    CommandHandler
)
from core.pugbot import PugBot
import os

api_key = os.getenv('TOKEN')

def start(bot, update):
    message = 'Olá! Sou o Bot do Python User Group - MA (PUGMA) '
    bot.send_message(chat_id=update.message.chat_id, text=message)

def hello_new_users(bot, update):
    new_chat_members = update.message.new_chat_members

    for member in new_chat_members:
        print(member.username)
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
    bot.send_message(
        chat_id=update.message.chat_id,
        text=lastMeetup['text'],
        parse_mode='html',
        photo=lastMeetup['photo']
    )


def main():
    updater = Updater(token=api_key)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    new_user_handler = MessageHandler(
        Filters.status_update.new_chat_members,
        hello_new_users
    ) 
    last_meetup = CommandHandler('last_meetup', last_meetup)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(new_user_handler)
    dispatcher.add_handler(last_meetup)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()