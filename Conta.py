class Conta:
    saldo: float
    numero: int
    agencia: str
    # cliente: Cliente
    # historico: Historico

    def saldo(self) -> float:
        pass

    # def nova_conta(self, cliente: Cliente, numero: int) -> Conta:
    #     pass

    def sacar(self, valor: float) -> bool:
        pass

    def depositar(self, valor: float) -> bool:
        pass
