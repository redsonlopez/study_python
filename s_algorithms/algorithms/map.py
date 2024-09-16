print("Exemplo 1")
linguagens = '''PYTHON JAVA JAVASCRIPT C C# C++ SWIFT GO KOTLIN'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {nova_lista}")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

print("\nExemplo 2")
numeros = [0, 1, 2, 3, 4, 5]

quadrados = list(map(lambda x: x*x, numeros))
print(f"Lista com o número elevado a ele mesmo = {quadrados}")

