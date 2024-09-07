import numpy

matriz_1_1 = numpy.array([1, 2, 3]) # Cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # Cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Cria matriz 2 linhas e 3 colunas
m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) # Cria matriz 2 X 5 com números inteiros

print(type(matriz_1_1))

print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)

print('\n m4 = \n', m4)
print(f"Soma dos valores em m4 = {m4.sum()}")
print(f"Valor mínimo em m4 = {m4.min()}")
print(f"Valor máximo em m4 = {m4.max()}")
print(f"Média dos valores em m4 = {m4.mean()}")

