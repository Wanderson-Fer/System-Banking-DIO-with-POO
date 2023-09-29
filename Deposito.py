from Conta import Conta
from Transacao import Transacao


class Deposito(Transacao):
    _valor: float

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
