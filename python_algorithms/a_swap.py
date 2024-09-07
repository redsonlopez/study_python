ordenar= [7, 3] 
print(f"Lista a ordenar= {ordenar}")

if ordenar[0] > ordenar[1]:
	swap= ordenar[0]
	ordenar[0]= ordenar[1]
	ordenar[1]= swap
print(f"Lista ordenada= {ordenar}")

