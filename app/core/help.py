# -*- coding: utf-8 -*-
#
from functools import wraps


class Help:

    lista_comando = []

    class __Help:
        def __init__(self):
            self.lista_comando = []

        def __lista__(self):
            return self.lista_comando

    instance = None

    def __init__(self):
        if not Help.instance:
            Help.instance = Help.__Help()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def command_doc(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        """Captura a descricao da funcao e registra para o comando /help"""
        h = Help()
        h.lista_comando.append("{}".format(func.__doc__))

        return wrapper
