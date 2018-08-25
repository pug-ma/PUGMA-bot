import requests
import json
from app.api_github import Github 


class TestGithub:
    user = 'pug-ma'
    repository = 'meetups'
    base_url = 'https://api.github.com/repos'
        
    def test_repository(self):
        response = requests.get(f'{self.base_url}/{self.user}/{self.repository}')
        
        assert 200 == response.status_code
    
    def test_encontro_download_url(self):
        download_url = 'https://raw.githubusercontent.com/pug-ma/meetups/master/encontros/PUG-MA%20%2302.jpg'
        api = Github()

        assert download_url == api.photo_encontro('2')

    def test_last_encontro_download_url(self):
        download_url = 'https://raw.githubusercontent.com/pug-ma/meetups/master/encontros/meetups_info.json'
        api = Github()

        assert download_url == api.photo_last_encontro()
