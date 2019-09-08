import json

import pytest
import requests

from bot.configuration import GithubData
from bot.utils import photo_meetup

github_data = GithubData()
contents_url = f"{github_data.url}/contents/palestras?ref=master"


def test_repository():
    response = requests.get(github_data.url, headers=github_data.headers)

    assert 200 == response.status_code


def test_encontro_download_url():
    download_url = "https://raw.githubusercontent.com/pug-ma/meetups/master/palestras/PUG-MA%20%2302.jpg"
    cmd = ["#meetup", "1"]

    result, num = photo_meetup(github_data, cmd)

    assert download_url == result


def test_last_encontro_download_url():
    response = requests.get(contents_url, headers=github_data.headers)

    content = json.loads(response.content)
    content_length = len(content)

    last_photo_url = content[-1].get("download_url")

    cmd = ["#meetup"]

    result, num = photo_meetup(github_data, cmd)

    assert last_photo_url == result
