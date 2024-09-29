import sys

conta_poupanca= False
conta_corrente= True

saldo= 1180
cheque_especial= 500

saque= float(input("Digite o valor do saque: "))

if conta_poupanca:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
if conta_corrente:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif (saldo + cheque_especial) >= saque:
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")
else:
    sys.exit("Opção Invalida")

