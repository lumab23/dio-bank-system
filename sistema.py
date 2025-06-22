import textwrap

def menu():
    menu = """
    ============== MENU ==============
    [d]\t - DEPOSITAR
    [s]\t - SACAR
    [e]\t - EXTRATO
    [q]\t - SAIR
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nO valor do saque execede o limite.")
    elif excedeu_saques:
        print("\nUltrapassou o número máximo de saques.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0


    while True:

        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Informe o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe o valor do saque: R$"))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "q":
            print("\nObrigado por usar o sistema! Saindo...")
            break

        else: 
            print("Operação inválida. Tente novamente.")

main()