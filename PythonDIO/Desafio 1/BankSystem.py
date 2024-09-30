# Inicialização das variáveis
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saque
extrato = ""  # Armazenar as movimentações da conta
numero_saques = 0  # Contador de saques diários
LIMITE_SAQUES = 3  # Limite diário de saques

# Menu de opções para o usuário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

# Loop principal para manter o sistema em execução até que o usuário saia
while True:
    opcao = input(menu)  # Recebe a opção escolhida pelo usuário

    # Depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é positivo
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Armazena a operação no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        # Verificações para garantir que o saque pode ser realizado
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque é maior que o saldo disponível
        excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques diários foi atingido

        # Condições para impedir o saque
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor  # Subtrai o valor do saque do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Armazena a operação no extrato
            numero_saques += 1  # Incrementa o número de saques realizados
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Extrato
    elif opcao == "3":
        # Exibe todas as movimentações e o saldo atual
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Sair do sistema
    elif opcao == "4":
        break  # Encerra o loop e, consequentemente, o sistema

    # Caso o usuário escolha uma opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")