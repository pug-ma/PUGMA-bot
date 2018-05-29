from decouple import config
import logging

# Bot keys settings
API_KEY = config('TOKEN')
APP_NAME = config('APP_NAME')
PORT = config('PORT', default='8443', cast=int)


# Logging settings
DEBUG = config('DEBUG', default=False, cast=bool)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG if DEBUG else logging.NOTSET)
