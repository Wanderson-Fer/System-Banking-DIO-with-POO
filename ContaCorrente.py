from Conta import Conta
from PessoaFisica import PessoaFisica
from Saque import Saque


class ContaCorrente(Conta):
    limite: float
    limite_saques: int

    def __int__(self, numero, cliente: PessoaFisica, limite=500, limite_saques=3):
        super.__init__(numero, cliente)

        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = len(
            [
                transacao for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('Operação falhou!')
            print('O valor do saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou!')
            print('Número máximo de saques excedido.')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\n\n{self.numero}
            Titular:\t{self.cliente.nome}
        """
