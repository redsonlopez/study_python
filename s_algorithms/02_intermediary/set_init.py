numeros= set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
print(numeros)

letras= set("abacaxi") # {"b", "a", "c", "x", "i"}
print(letras)

carros= set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}
print(carros)

linguagens= {"python", "java", "python"}
print(linguagens)

l_numeros= list(numeros)
print(l_numeros[0])

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

conjunto_a= {1, 2, 3}
conjunto_b= {2, 3, 4}
conjunto_c= {4, 1, 2, 5, 6, 3}
conjunto_d= {7, 8, 9}

uniao= conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
print(uniao)

intercessao= conjunto_a.intersection(conjunto_b) # {2, 3}
print(intercessao)

diferenca_a= conjunto_a.difference(conjunto_b) # {1}
diferenca_b= conjunto_b.difference(conjunto_a) # {4}
print(f"Diferença dos conjuntos:\na: {diferenca_a}\nb: {diferenca_b}")

diferenca_simetrica= conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
print(diferenca_simetrica)

subconjunto_a= conjunto_a.issubset(conjunto_c) # True
subconjunto_c= conjunto_c.issubset(conjunto_a) # False
print(f"São subconjuntos?\na: {subconjunto_a}\nc: {subconjunto_c}")

superconjunto_a= conjunto_a.issuperset(conjunto_c) # False
superconjunto_c= conjunto_c.issuperset(conjunto_a) # True
print(f"São superconjuntos?\na: {superconjunto_a}\nc: {superconjunto_c}")

disjunto_d= conjunto_c.isdisjoint(conjunto_d) # True
disjunto_b= conjunto_c.isdisjoint(conjunto_b) # False
print(f"O conjunto c é disjunto dos conjuntos:\nd: {disjunto_d}\nb: {disjunto_b}")

sorteio= {1, 3, 23}

sorteio.add(25) # {1, 3, 25, 23}

sorteio.add(42) # {1, 3, 42, 23, 25}
sorteio.add(25) # {1, 3, 42, 23, 25}

sorteio.discard(1) # {3, 42, 23, 25}
sorteio.discard(9) # {3, 42, 23, 25}

sorteio.pop() # 3
sorteio.pop() # 42
print(sorteio)

sorteio.remove(25)
print(sorteio)

