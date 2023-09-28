from Cliente import Cliente
from datetime import date


class PessoaFisica(Cliente):
    cpf: str
    nome: str
    data_nascimento: date

    def __init__(self, nome: str, data_nascimento: date, cpf: str, endereco: str):
        super().__init__(endereco)

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
