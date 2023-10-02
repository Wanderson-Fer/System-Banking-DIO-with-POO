from datetime import datetime
from Transacao import Transacao


class Historico:
    _transacao: list

    def __init__(self):
        self._transacao = []

    @property
    def transacoes(self) -> list:
        return self._transacao

    def adicionar_transacao(self, transacao: Transacao):
        self._transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().
                strftime("%d-%m-%Y %H:%M:%s")
            }
        )
