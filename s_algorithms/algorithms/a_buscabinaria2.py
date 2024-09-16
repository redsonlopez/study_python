nomes = ["Hedson", "Aline", "Charlotte"]

def procurar_valor(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return meio
    return None

resultado = procurar_valor(lista=nomes, valor='Aline')
if resultado:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")

