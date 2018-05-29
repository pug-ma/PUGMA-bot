from decouple import config


API_KEY = config('TOKEN')
APP_NAME = config('APP_NAME')
PORT = config('PORT', default='8443', cast=int)
