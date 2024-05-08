import textwrap


def menu(): 
    menu = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ->  """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    print('-' * 30)
    print(f"{'DEPÓSITO':^30}")
    print('-' * 30)
    if valor < 0:
        print("Valor negativo, não foi possível depositar.")
    else:
        saldo += valor
        extrato += f"R${valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print('-' * 30)
    print(f"{'SAQUE':^30}")
    print('-' * 30)
    if valor <= saldo:
        if valor <= limite:
            if numero_saques < limite_saques:
                saldo -= valor
                numero_saques += 1
                extrato += f"-R${valor:.2f}\n"
                print("Valor sacado com sucesso!")
                print(f"Número de saques no dia: {numero_saques}")
            else:
                print("Não foi possível sacar. Limite de saques atingido.")
        else:
            print("Não foi possível sacar. Saque acima do valor limite: R$500,00.")
    else:
        print("Não foi possível sacar. Saldo insuficiente.")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('-' * 30)
    print(f"{'EXTRATO':^30}")
    print('-' * 30)
    print(extrato)
    print(f"SALDO: R${saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Infomre o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd=mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criado com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Tiutlar:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
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
             print("Opção INVÁLIDA! Por favor, selecione novamente a operação desejada.")

main()