from datetime import datetime

# Listas para armazenar usuários e contas
usuarios = []  # Lista de usuários
contas = []  # Lista de contas bancárias
saldo_contas = {}  # Dicionário para armazenar saldo das contas
extrato_contas = {}  # Dicionário para armazenar extrato das contas
numero_saques_conta = {}  # Dicionário para armazenar número de saques por conta

# Variáveis fixas
LIMITE_SAQUES = 3  # Limite diário de saques
LIMITE_TRANSACOES = 10  # Limite de transações diárias
AGENCIA_FIXA = "0001"  # Agência fixa para todas as contas

# Função para cadastrar usuário
def cadastrar_usuario(nome, nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário com esse CPF já existe!")
            return False
    usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return True

# Função para cadastrar conta bancária
def cadastrar_conta(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            numero_conta = len(contas) + 1  # Conta sequencial
            conta = {
                'agencia': AGENCIA_FIXA,
                'numero': numero_conta,
                'usuario': usuario
            }
            contas.append(conta)
            saldo_contas[numero_conta] = 0  # Inicializa saldo em zero
            extrato_contas[numero_conta] = ""  # Inicializa extrato vazio
            numero_saques_conta[numero_conta] = 0  # Inicializa contagem de saques
            print(f"Conta {numero_conta} vinculada ao usuário {usuario['nome']}!")
            return True
    print("CPF não encontrado! Cadastro da conta não realizado.")
    return False

# Função de depósito (por posição)
def depositar(conta_idx, valor):
    if valor > 0:
        saldo_contas[conta_idx] += valor  # Adiciona o valor ao saldo
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém data e hora da transação
        extrato_contas[conta_idx] += f"[{data_hora}] Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta_idx}!")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função de saque (por nome)
def sacar(nome, valor):
    for conta in contas:
        if conta['usuario']['nome'] == nome:
            conta_idx = conta['numero']
            if valor <= 0:
                print("Operação falhou! O valor informado é inválido.")
            elif saldo_contas[conta_idx] < valor:
                print("Operação falhou! Saldo insuficiente.")
            elif valor > 500:
                print("Operação falhou! O valor excede o limite de R$500.")
            elif numero_saques_conta[conta_idx] >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques diários atingido.")
            else:
                saldo_contas[conta_idx] -= valor
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato_contas[conta_idx] += f"[{data_hora}] Saque: R$ {valor:.2f}\n"
                numero_saques_conta[conta_idx] += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta_idx}!")
            return
    print(f"Usuário {nome} não encontrado ou não possui conta ativa.")

# Função de extrato (por posição e nome)
def extrato(conta_idx=None, nome=None):
    if conta_idx:
        if conta_idx in extrato_contas:
            print("\n================ EXTRATO ================")
            print(extrato_contas[conta_idx] if extrato_contas[conta_idx] else "Não foram realizadas movimentações.")
            print(f"Saldo: R$ {saldo_contas[conta_idx]:.2f}")
            print("==========================================")
        else:
            print("Conta não encontrada!")
    elif nome:
        for conta in contas:
            if conta['usuario']['nome'] == nome:
                conta_idx = conta['numero']
                print("\n================ EXTRATO ================")
                print(extrato_contas[conta_idx] if extrato_contas[conta_idx] else "Não foram realizadas movimentações.")
                print(f"Saldo: R$ {saldo_contas[conta_idx]:.2f}")
                print("==========================================")
                return
        print(f"Usuário {nome} não encontrado ou não possui conta ativa.")
    else:
        print("Por favor, informe o nome ou o número da conta.")

# Função para listar os usuários cadastrados (para testes)
def listar_usuarios():
    if usuarios:
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}")
    else:
        print("Nenhum usuário cadastrado.")

# Função para listar as contas cadastradas (para testes)
def listar_contas():
    if contas:
        for conta in contas:
            print(f"Conta: {conta['numero']}, Agência: {conta['agencia']}, Titular: {conta['usuario']['nome']}")
    else:
        print("Nenhuma conta cadastrada.")