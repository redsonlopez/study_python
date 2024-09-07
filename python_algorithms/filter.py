numeros  = list(range(0, 21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

numeros_pares2 = list(map(lambda x: x % 2 == 0, numeros))
print(numeros_pares2)

