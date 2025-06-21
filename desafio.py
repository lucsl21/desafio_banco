def menu_principal():
    return input("""
[u] Cadastrar usuário
[c] Criar nova conta
[l] Listar contas
[s] Selecionar conta para operações
[q] Sair

=> """)

def menu_conta():
    return input("""
[d] Depositar
[s] Sacar
[e] Extrato
[v] Voltar

=> """)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ").strip()

    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já cadastrado.")
        return

    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()

    usuarios.append({"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def encontrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)

def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = encontrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Cadastre primeiro.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "saques": 0
    })
    print(f"Conta criada com sucesso! Número: {numero_conta}")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")

def selecionar_conta(contas):
    numero = int(input("Informe o número da conta: "))
    conta = next((c for c in contas if c["numero_conta"] == numero), None)
    if conta:
        menu_operacoes(conta)
    else:
        print("Conta não encontrada.")

def depositar(conta):
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado.")
    else:
        print("Valor inválido.")

def sacar(conta, limite=500, limite_saques=3):
    valor = float(input("Valor do saque: "))
    if valor <= 0:
        print("Valor inválido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Excede o limite de saque.")
    elif conta["saques"] >= limite_saques:
        print("Limite de saques diário atingido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques"] += 1
        print("Saque realizado.")

def exibir_extrato(conta):
    print("\n========= EXTRATO =========")
    print(conta["extrato"] if conta["extrato"] else "Sem movimentações.")
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("===========================")

def menu_operacoes(conta):
    while True:
        opcao = menu_conta()

        if opcao == "d":
            depositar(conta)
        elif opcao == "s":
            sacar(conta)
        elif opcao == "e":
            exibir_extrato(conta)
        elif opcao == "v":
            break
        else:
            print("Opção inválida.")

def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu_principal()

        if opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            criar_conta(AGENCIA, contas, usuarios)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "s":
            selecionar_conta(contas)
        elif opcao == "q":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

main()
