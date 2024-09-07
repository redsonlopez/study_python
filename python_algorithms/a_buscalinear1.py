import random
lista = random.sample(range(1000), 50)
print(sorted(lista))

def buscalinear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
    return False

print(buscalinear(lista, 10))

