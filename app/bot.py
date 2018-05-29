"""Modulo principal do BOT."""
from telegram.ext import Updater
from settings import (
    API_KEY,
    APP_NAME,
    PORT
)
from handlers import (
    START,
    NEW_USER,
    LAST_MEETUP,
    MEETUP,
    RULES
)


def main():
    """Rotina principal de iniciação do BOT."""
    updater = Updater(token=API_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(START)
    dispatcher.add_handler(NEW_USER)
    dispatcher.add_handler(LAST_MEETUP)
    dispatcher.add_handler(MEETUP)
    dispatcher.add_handler(RULES)

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
