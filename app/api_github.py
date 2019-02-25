import requests
import json


class Github:
    def __init__(self):
        self.user = 'pug-ma'
        self.repository = 'meetups'
        self.base_url = 'https://api.github.com/repos'
        self.headers = {
            'user-agent': self.user
        }

    def _name_encontro(self, index):
        if len(index) == 1:
            index = '0' + index

        return requests.utils.quote(f'PUG-MA #{index}.jpg')

    def photo_encontro(self, index):
        url = f'{self.base_url}/{self.user}/{self.repository}/contents/palestras/{self._name_encontro(index)}'

        response = requests.get(url, headers=self.headers)
        content = json.loads(response.content)
        
        return content.get('download_url')

    def photo_last_encontro(self):
        url = f'{self.base_url}/{self.user}/{self.repository}/contents/palestras/'

        response = requests.get(url, headers=self.headers)
        content = json.loads(response.content)

        return content[-1].get('download_url')
