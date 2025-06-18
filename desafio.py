menu = """

 🏦 Banco Santander   
══════════════════════
 [d] Depositar 💰     
 [s] Sacar 💸         
 [e] Extrato 📜       
 [q] Sair 🚪           
══════════════════════
👉 Digite sua escolha: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        try:
            valor = float(input("Quanto você quer depositar? R$ "))
            if valor > 0:
                saldo += valor
                extrato += f"💰 Depósito: R$ {valor:.2f}\n"
                print(f"R$ {valor:.2f} depositados com sucesso!")
            else:
                print("Valor inválido. Tente novamente!")
        except:
            print("Favor digitar um número válido!")

    elif opcao == "s":
        try:
            valor = float(input("Quanto você quer sacar? R$ "))
            
            sem_grana = valor > saldo
            passou_limite = valor > limite
            muitos_saques = numero_saques >= LIMITE_SAQUES

            if sem_grana:
                print("Saldo insuficiente!")
            elif passou_limite:
                print("Esse valor passa seu limite por saque!")
            elif muitos_saques:
                print("Parece que você já fez saques demais por hoje!")
            elif valor > 0:
                saldo -= valor
                extrato += f"💸 Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"R$ {valor:.2f} sacados. Até mais!")
            else:
                print("Valor inválido!")
        except:
            print("Favor digitar um número válido!")

    elif opcao == "e":
        print("\n📋 EXTRATO BANCÁRIO 📋")
        print("-----------------------------")
        print("Nada aconteceu ainda..." if not extrato else extrato)
        print(f"\nSeu saldo: R$ {saldo:.2f}")
        print("-----------------------------")
        print("Fim do extrato! 😊")

    elif opcao == "q":
        print("Até logo! Volte sempre ao Banco Santander! 🎉")
        break

    else:
        print("Atenção! Essa opção não existe! Tente de novo, por favor!")