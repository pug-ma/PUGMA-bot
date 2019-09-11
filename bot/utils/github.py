"""
Modulo dedicado a classes/funções sem nenhuma outra dependência ou
que não sejam parte do core do Bot.
"""
import json

import requests


def photo_meetup(repo_data, matches):
    """
    Recebe como entrada uma Dataclass com dados do nosso
    repositório no Github e retorna a url de uma imagem
    do meetup.
    """
    contents_url = f"{repo_data.url}/contents/palestras?ref=master"

    response = requests.get(contents_url, headers=repo_data.headers)
    content = json.loads(response.content)
    content_length = len(content)

    if len(matches) == 1:
        # /meetup retorna sempre o último
        return content[-1].get("download_url"), (content_length)
    elif int(matches[1]) < content_length:
        # /meetup \d{1,2}
        event_num = int(matches[1])
        return content[event_num - 1].get("download_url"), event_num
    else:
        # Numero invalido
        return None, None
