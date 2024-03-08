import textwrap

from ContaCorrente import ContaCorrente
from Deposito import Deposito
from PessoaFisica import PessoaFisica
from Saque import Saque


def menu() -> str:
    textmenu = """
    ================== MENU ==================
    [d]   Depositar
    [s]   Sacar
    [e]   Extrato
    [nc]  Nova Conta
    [lc]  Listar Contas
    [nu]  Novo Usuário
    [q]   Sair
    => """

    return input(textwrap.dedent(textmenu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [
        cliente for cliente in clientes if cliente.cpf == cpf
    ]

    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return

    # FIXME: não permite escolher conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor de depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("==================== EXTRATO ====================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movintenções"
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao["tipo"]}:\tR$ {transacao["valor"]:.2f}'

    print(extrato)
    print(f'\nSaldo:\tR$ {conta.saldo:.2f}')
    print("=================================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('Já existe cliente com esse CPF!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a dara de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereco (logradouro, nro - bairro - cidade/UF): ')

    cliente = PessoaFisica(
        nome=nome,
        data_nascimento=data_nascimento,
        cpf=cpf,
        endereco=endereco
    )

    clientes.append(cliente)

    print('\nCliente cadastrado com sucesso!')


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = ContaCorrente.nova_conta(numero=numero_conta, cliente=cliente)
    print('x'*100)
    print(str(conta))
    print('x'*100)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


if __name__ == '__main__':
    list_clientes = []
    list_contas = []

    while True:
        opcao = menu()

        match opcao:
            case "d":
                depositar(list_clientes)

            case "s":
                sacar(list_clientes)

            case "e":
                exibir_extrato(list_clientes)

            case "nu":
                criar_cliente(list_clientes)

            case "nc":
                nro_conta = len(list_contas) + 1
                criar_conta(nro_conta, list_clientes, list_contas)

            case "lc":
                listar_contas(list_contas)

            case "q":
                break

            case _:
                print("Operação inválida!")
                print("Por favor selecione uma ooperação do menu.\n")
