"""
Testes do módulo /bot/utils.py, relacionados à interações
com a API do Github
"""

import json

import pytest
import requests

from bot.configuration import GithubData
from bot.utils import photo_meetup

github_data = GithubData()
contents_url = f"{github_data.url}/contents/palestras?ref=master"


def test_repository():
    """
    Testa se a API e os repositórios do PUG estão OK
    """
    response = requests.get(github_data.url, headers=github_data.headers)

    assert response.status_code == 200


def test_encontro_download_url():
    """
    Testa se o commando /meetup 1 retorna o primeiro meetup
    registrado no repo 'Meetups'.
    """
    download_url = (
        "https://raw.githubusercontent.com/pug-ma/"
        "meetups/master/palestras/PUG-MA%20%2302.jpg"
    )
    cmd = ["/meetup", "1"]

    result, _ = photo_meetup(github_data, cmd)

    assert download_url == result


@pytest.mark.xfail
def test_last_encontro_download_url():
    """
    Testa se o commando /meetup retorna o último meetup
    registrado no repo 'Meetups'.
    """
    response = requests.get(contents_url, headers=github_data.headers)

    content = json.loads(response.content)

    last_photo_url = content[-1].get("download_url")

    cmd = ["/meetup"]

    result, _ = photo_meetup(github_data, cmd)

    assert last_photo_url == result
