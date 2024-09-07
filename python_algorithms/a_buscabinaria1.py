def buscabinaria(lista, valor):
	minimo = 0
	maximo = len(lista) - 1
	while minimo <= maximo:
		meio = (minimo + maximo) // 2
		if valor < lista[meio]:
			maximo = meio - 1
		elif valor > lista[meio]:
			minimo = meio + 1
		else:
			return True
	return False

lista = list(range(1, 50))
print(lista)

print('\n',buscabinaria(lista=lista, valor=10))
print('\n', buscabinaria(lista=lista, valor=200))


