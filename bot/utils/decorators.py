"""
Modulo dedicado a classes/funções sem nenhuma outra dependência ou
que não sejam parte do core do Bot.
"""


def hidden(func):
    """
    Decorator que adiciona um atributo 'is_hidden' na função
    em que é aplicado. É utilizado no módulo `core.py` para
    ocultar certos comandos.
    """

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper.is_hidden = True
    return wrapper
