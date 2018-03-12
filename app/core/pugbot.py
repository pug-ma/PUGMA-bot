import requests
import json
import os

BOLD = lambda k: '<b>' + k + '</b>'
PARAGRAPH = lambda k, v: BOLD(k) + ': ' + v

class PugBot():
    """
    PugBot() irá recolher da .env a URL para um arquivo JSON
    contendo um array com objetos referenciados aos eventos,
    o metodo lastEvent retorna um dict com dois elementos:

    text: uma saida valida em HTML das infos
    photo: URL do banner utilizado para o meetup 
    """
    def __init__(self):
        url = os.getenv('RAW_GIT_DOC_URL')
        if not url:
            raise Exception('Unable to load the events data, empty source URL')
        self.URL = url
        self.DOC_INFO = json.loads(requests.get(self.URL).content) 
    
    def _get_last_event(self): 
        return self.DOC_INFO[-1]
    
    def lastEvent(self):
        event = self._get_last_event()
        photo = event.pop('photo_url')
        text = ''.join([PARAGRAPH(k, v) in event.items()])
        message = {'text': text, 'photo': photo}
        return message
        


        
        
        



