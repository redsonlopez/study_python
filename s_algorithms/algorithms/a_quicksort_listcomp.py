def quicksort(lista):
    if len(lista) <= 1: return lista
    pivo = lista[0]
    iguais  = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor <  pivo]
    maiores = [valor for valor in lista if valor >  pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


lista = [10, 9, 5, 8, 11, -1, 3]
print(quicksort(lista))

