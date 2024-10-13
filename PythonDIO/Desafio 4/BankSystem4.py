import textwrap

# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0


# Classe para gerenciar as operações bancárias (depósito, saque, extrato)
class OperacaoBancaria:
    LIMITE_SAQUES = 3
    LIMITE_SAQUE = 500

    @staticmethod
    def depositar(conta, valor):
        if valor > 0:
            conta.saldo += valor
            conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    @staticmethod
    def sacar(conta, valor):
        excedeu_saldo = valor > conta.saldo
        excedeu_limite = valor > OperacaoBancaria.LIMITE_SAQUE
        excedeu_saques = conta.numero_saques >= OperacaoBancaria.LIMITE_SAQUES

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            conta.saldo -= valor
            conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            conta.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    @staticmethod
    def exibir_extrato(conta):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
        print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
        print("==========================================")


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = Cliente(nome, cpf, data_nascimento, endereco)
    usuarios.append(novo_usuario)
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = ContaBancaria(agencia, numero_conta, usuario)
        print("\n=== Conta criada com sucesso! ===")
        return conta
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\nAgência:\t{conta.agencia}
        C/C:\t\t{conta.numero_conta}
        Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta.numero_conta == numero_conta), None)

            if conta:
                valor = float(input("Informe o valor do depósito: "))
                OperacaoBancaria.depositar(conta, valor)
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "s":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta.numero_conta == numero_conta), None)

            if conta:
                valor = float(input("Informe o valor do saque: "))
                OperacaoBancaria.sacar(conta, valor)
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "e":
            numero_conta = int(input("Informe o número da conta: "))
            conta = next((conta for conta in contas if conta.numero_conta == numero_conta), None)

            if conta:
                OperacaoBancaria.exibir_extrato(conta)
            else:
                print("\n@@@ Conta não encontrada. @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()