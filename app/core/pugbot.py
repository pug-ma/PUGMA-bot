"""Modulo com principais funcionalidades do PUG-MA Bot."""
import requests
import json
from settings import DOC_URL, REGRAS_URL
from api_github import Github


class PugBot():
    """Classe com todos os métodos referentes ao uso do bot do PUG-MA."""

    def __init__(self):
        self.api = Github()
        self._url = DOC_URL
        self._regras_url = REGRAS_URL

        if not self._url or not self._regras_url:
            raise Exception('Unable to load the events data, empty source URL')

        self._doc_info = json.loads(requests.get(self._url).content)
        self._regras = requests.get(self._regras_url).content.decode()

    def _get_last_event(self):
        """Filtra o último evento do grupo."""
        return self._doc_info[-1]

    def last_event(self):
        """Retorna o último evento do grupo com Descrição e Banner."""
        event = self._get_last_event()
        photo = event.pop('photo_url')
        text = 'Meetup PUG-MA'
        message = {'text': text, 'photo': photo}
        return message

    def event(self, index):
        """
        Retorna um evento específico baseado
        no seu index/número do meetup.
        """
        photo = self.api.photo_encontro(str(index))
        text = 'Meetup PUG-MA'
        message = {'text': text, 'photo': photo}
        return message

    def regras(self):
        """
        Retorna as regras que os administradores
        usam para manter o grupo.
        """
        return self._regras
