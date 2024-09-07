def selection_sort(lista):
	n = len(lista)
	i = 0
	
	while i < n:
		index_menor = i
		j = i + 1

		while j < n:
			if lista[j] < lista[index_menor]:
				index_menor = j
			j += 1
		
		swap = lista[i]
		lista[i] = lista[index_menor]
		lista[index_menor] = swap
		
		i += 1
	
	return lista

lista = [10, 9, 5, 8, 11, -1, 3]
print(selection_sort(lista))

