###

lista= [2, 17, 6, 5, 24, 12, 121, 157, 23]

def busca(lista, valor):
    for busca in lista:
        if valor in lista:
            return True
        else:
            return False

print(busca(lista, 121))

