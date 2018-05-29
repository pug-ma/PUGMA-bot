from decouple import config
import logging

# Bot keys settings
API_KEY = config('TOKEN')
APP_NAME = config('APP_NAME')
PORT = config('PORT', default='8443', cast=int)

# PugBot url settings
RAW_GIT_DOC_URL = config('RAW_GIT_DOC_URL')
REGRAS_URL = config('RAW_GIT_DOC_URL')


# Logging settings
DEBUG = config('DEBUG', default=False, cast=bool)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger()

if DEBUG:
    LOGGER.setLevel(logging.DEBUG)
