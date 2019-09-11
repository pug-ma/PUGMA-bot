"""Configurações do projeto."""
from dataclasses import dataclass, field


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
