linguagens= ["C", "C++", "Fortran"]

def buscalinear(lista, busca):
	for valor in lista:
		if valor == busca:
			return True
	return False

print(buscalinear(linguagens, "C++"))

