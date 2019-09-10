"""Configurações do projeto."""
import os
from dataclasses import dataclass, field

from decouple import config


@dataclass
class BaseConfig:
    """
    Classe com parâmetros para configuração do Bot
    """

    # ID e HASH são disponibilizados ao registar um app no Telegram
    # Nós não fornecemos os dados do projeto do bot em produção, consulte
    # o seguinte link e crie o seu próprio para testar localmente:
    api_id: str = config("API_ID")
    api_hash: str = config("API_HASH")
    # Nome do app quando for fazer o deploy no Heroku
    app_name: str = config("APP_NAME")
    # Token gerado pelo @botfather
    token: str = config("TOKEN")
    # Variável para modo DEBUG, por segurança setar como False para produção
    debug: bool = config("DEBUG", cast=bool)
    # Session
    session: str = config("SESSION_STRING")
    # Markdown com as regras do grupo
    regras: str = os.path.join(os.path.abspath(".."), "REGRAS.md")
    # Valores para que o bot consiga usar sticker
    stickerset_id: int = config("STICKERSET_ID", cast=int)
    stickerset_hash: int = config("STICKERSET_HASH", cast=int)


@dataclass
class GithubData:
    """
    Classe com os dados da organização do PUGMA
    no Github.
    """

    user: str = "pug-ma"
    repository: str = "meetups"
    base_url: str = "https://api.github.com/repos"
    url: str = field(init=False)
    headers: dict = field(init=False)

    def __post_init__(self):
        self.url: str = f"{self.base_url}/{self.user}/{self.repository}"
        self.headers: dict = {"user-agent": self.user}


github_data = GithubData()

settings = BaseConfig()
