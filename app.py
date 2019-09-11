from bot import Bot, settings

if __name__ == "__main__":
    Bot.start(bot_token=settings.token)

    Bot.run_until_disconnected()
