"""Modulo principal do BOT."""
from telegram.ext import Updater
from settings import API_KEY
from handlers import (
    start_handler,
    new_user_handler,
    last_meetup_handler,
    meetup_handler,
    regras_handler
)


def main():
    """Rotina principal de iniciação do BOT."""
    updater = Updater(token=API_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(new_user_handler)
    dispatcher.add_handler(meetup_handler)
    dispatcher.add_handler(last_meetup_handler)
    dispatcher.add_handler(regras_handler)

    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=API_KEY
    )

    updater.bot.set_webhook(f'https://{APP_NAME}.herokuapp.com/{API_KEY}')
    #updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
