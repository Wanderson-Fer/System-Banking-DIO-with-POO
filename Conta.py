from Cliente import Cliente
from Historico import Historico


class Conta:
    _saldo: float
    _numero: int
    _agencia: str
    _cliente: Cliente
    _historico: Historico

    def __init__(self, numero: int, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    def sacar(self, valor: float) -> bool:
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Operação Falhou!')
            print('Saldo insuficiente.')
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso!')
            return True
        else:
            print('Operação falhou!')
            print('O valor informado é inválido.')

        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print('Depósito Realizado com sucesso!')
        else:
            print('Operação falhou!')
            print('O valor informado é inválido.')
            return False

        return True
