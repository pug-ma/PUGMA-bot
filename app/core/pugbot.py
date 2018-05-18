import requests
import json
from decouple import config

# BOLD = lambda k: '<b>' + k + '</b>'
# PARAGRAPH = lambda k, v: BOLD(k) + ': ' + v


class PugBot():
    """
    PugBot() irá recolher da .env a URL para um arquivo JSON
    contendo um array com objetos referenciados aos eventos,
    o metodo lastEvent retorna um dict com dois elementos:

    text: uma saida valida em HTML das infos
    photo: URL do banner utilizado para o meetup
    """

    def __init__(self):
        self.url = config('RAW_GIT_DOC_URL')
        self.regras_url = config('REGRAS_URL')

        if not self.url or not self.regras_url:
            raise Exception('Unable to load the events data, empty source URL')

        self.doc_info = json.loads(requests.get(self.url).content)
        self._regras = requests.get(self.regras_url).content.decode()

    def _get_last_event(self):
        return self.doc_info[-1]

    def last_event(self):
        event = self._get_last_event()
        photo = event.pop('photo_url')
        text = 'Meetup PUG-MA'
        # text = ''.join([PARAGRAPH(k, v) in event.items()])
        message = {'text': text, 'photo': photo}
        return message

    def event(self, index):
        event = self.doc_info[index]
        photo = event.pop('photo_url')
        text = 'Meetup PUG-MA'
        message = {'text': text, 'photo': photo}
        return message

    def regras(self):
        return self._regras
