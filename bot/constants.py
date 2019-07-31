import os

WELCOME = {
    "pugma": "Este é o Python User Group - MA (PUG-MA). "
    "Um grupo para a galera de Python do Maranhão (ou não) que "
    "queira interagir e ficar por dentro do que está rolando na "
    "cena de Python aqui."
}

SPAM = (
    "SPAM não é uma atitude bem vinda no grupo. O usuário será "
    "removido após 3 denúncias."
)

MEETUPS = lambda x: {}

RULES = open("REGRAS.md", "r").read()
