def bubble_sort(lista):
	n = len(lista) -1
	i = 0
	while i < n:
		j = 0
		while j < n:
			if lista[j] > lista[j + 1]:
				temp = lista[j]
				lista[j] = lista[j + 1]
				lista[j + 1] = temp
			j += 1
		i += 1
	return lista

lista = [10, 9, 5, 8, 11, -1, 3]
print(bubble_sort(lista))


