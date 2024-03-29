from Transacao import Transacao
from Conta import Conta


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
