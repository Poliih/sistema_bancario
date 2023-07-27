menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor do depósito: "))
        if deposito > 0:
            saldo = saldo + deposito
            extrato.append(f"Depósito: +R$ {deposito:.2f}")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")

    elif opcao == "s":
        saque = float(input("Valor do saque: "))
        if saque > 0:
            if numero_saques < LIMITE_SAQUES and saque <= saldo:
                saldo = saldo - saque
                extrato.append(f"Saque: -R$ {saque:.2f}")
                numero_saques += 1
            elif numero_saques >= LIMITE_SAQUES:
                print("Você excedeu o limite de saques no dia.")
            else:
                print("Você não possui saldo suficiente para esse saque.")
        else:
            print("Valor inválido. O saque deve ser maior que zero.")


    elif opcao == "e":

        if not extrato:

            print("Nenhuma movimentação registrada no extrato.")
            print("Saldo Atual: R$ {:.2f}\n".format(saldo))

        else:

            print("\nExtrato:")

            for item in extrato:
                print(item)

            print("Saldo Atual: R$ {:.2f}\n".format(saldo))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
