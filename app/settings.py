"""Configurações do projeto."""
from decouple import config


# Url para banners dos meetups
DOC_URL = config('RAW_GIT_DOC_URL')

# Url para regras do grupo
REGRAS_URL = config('REGRAS_URL')

# TOKEN do Telegram
API_KEY = config('TOKEN')

# Nome do app/bot
APP_NAME = config('APP_NAME')

# Variável para modo DEBUG, por segurança setar como False para produção
DEBUG = config('DEBUG')

# Porta que a aplicação irá rodar
PORT = config('PORT', default='8443', cast=int)
