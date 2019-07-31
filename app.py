from bot import bot, settings

if __name__ == "__main__":
    bot.start(bot_token=settings.token)

    bot.run_until_disconnected()
