import requests
import json
import os


class PugBot():
    def __init__(self):
        with os.getenv('RAW_GIT_DOC_URL') as url:
            if not url:
                raise Exception('Unable to load the events data, empty source URL')
            self.URL = url
            self.DOC_INFO = json.loads(requests.get(self.URL).content)
    
    def _get_last_event(self): 
        return self.DOC_INFO[-1]
    
    def lastEvent(self):
        self._get_last_event()

