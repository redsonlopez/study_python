lista= []
i= 0
while i < 11:
	lista.append(i)
	i= i + 1

def a_buscabinaria(lista, valor):
	minimo= 0
	maximo= len(lista) -1
	while minimo <= maximo:
		media= (minimo + maximo) // 2
		if valor > lista[media]:
			minimo = media +1
		elif valor < lista[media]:
			maximo = media -1
		else:
			return True
	return False

print(a_buscabinaria(lista, 9))


