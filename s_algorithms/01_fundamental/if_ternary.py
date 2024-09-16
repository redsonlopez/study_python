saldo= 1180
saque= float(input("Digite o valor do saque: "))

status= "Sucesso" if saque <= saldo else "Falha"

print(f"{status} ao realizar o saque!")

