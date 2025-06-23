import textwrap
import re

def menu():
    menu = """
    ============== MENU ==============
    [d]\t - DEPOSITAR
    [s]\t - SACAR
    [e]\t - EXTRATO
    [nc]\t - NOVA CONTA
    [lc]\t - LISTAR CONTAS
    [nu]\t - NOVO USUÁRIO
    [q]\t - SAIR
    => """

    return input(textwrap.dedent(menu))

def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)

def filtrar_usuario(cpf, usuarios): 
    cpf_limpo = limpar_cpf(cpf)
    users_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_limpo]
    return users_filtrados[0] if users_filtrados else None

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("já existe um usuário cadastrado com esse cpf")
        return 
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cpf_limpo = limpar_cpf(cpf)
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_limpo,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("\nUsuário criado com sucesso!")

def cadastrar_conta_bancaria(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        nova_conta = {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario,
            "saldo": 0,
            "limite": 500,
            "extrato": "",
            "numero_saques": 0,
            "limite_saques": 3
        }
        contas.append(nova_conta)
        print("\nConta criada com sucesso!")
        print(f"Agência: {agencia} | Conta: {numero_conta}")
    else: 
        print("\nUsuário não encontrado!")

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return 

    print("\n=============== LISTA DE CONTAS ===============")
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """
        print(textwrap.dedent(linha))
    print("=================================================")

def depositar(conta, valor):

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")

    return conta

def sacar(*, conta, valor):

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= conta["limite_saques"]

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nO valor do saque execede o limite.")
    elif excedeu_saques:
        print("\nUltrapassou o número máximo de saques.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque:\t\tR$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nO valor informado é inválido.")

    return conta

def exibir_extrato(conta):
    print(f"\n================ EXTRATO {conta['numero_conta']} ================")
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta["extrato"])
    print(f"\nSaldo:\t\tR$ {conta['saldo']:.2f}")
    print("==========================================")

def buscar_conta_por_numero(numero, contas):
    for conta in contas:
        if conta["numero_conta"] == numero:
            return conta
    return None

def main():
    AGENCIA= "0001"
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            cadastrar_conta_bancaria(AGENCIA, usuarios, contas)
        
        elif opcao == "lc":
            listar_contas(contas)

        
        elif opcao in ("d", "s", "e"):
            if not contas:
                print("\nNenhuma conta foi cadastrada ainda. Crie uma conta primeiro.")
                continue

            num_conta = int(input("Informe o número da conta: "))
            conta = buscar_conta_por_numero(num_conta, contas)

            if not conta:
                print("\nConta não encontrada!")
                continue

            if opcao == "d":
                valor = float(input("Informe o valor que deseja depositar: R$ "))
                conta = depositar(conta, valor)
            
            elif opcao == "s":
                valor = float(input("Informe o valor do saque: R$ "))
                conta = sacar(conta=conta, valor=valor)
            
            elif opcao == "e":
                exibir_extrato(conta)
        
        elif opcao == "q":
            print("\nObrigado por usar o sistema! Saindo...")
            break

        else: 
            print("Operação inválida. Tente novamente.")

if __name__ == "__main__":
    main()