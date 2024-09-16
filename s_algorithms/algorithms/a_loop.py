lista= []
numero= -3
while numero < 11:
	lista.append(numero)
	numero= numero + 1
print(f"Lista= {lista}")

lista.append(11.1)
pares= []
impares= []
for i in lista:
	if i % 2 == 0:
		pares.append(i)
	elif i % 2 == 1:
		impares.append(i)
	else:
		outro= i
print(f"Pares= {pares}\nImpares= {impares}\nOutro Valor= {outro}")


