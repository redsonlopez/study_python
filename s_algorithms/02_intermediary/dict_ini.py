pessoa= {"nome": "Hedson", "idade": "37"}

aninhado= {
        "db1": {"coluna1": "valor1", "coluna2": "valor2"},
        "db2": {"coluna1": "valor1", "coluna2": "valor2"},
}

aninhado2= {
        "chave1": {"chave2.1": {"chave3.1": "valor3.1"}, "chave2.2": {"chave3.2": {"chave4.1": "valor4.1"}}},
}

for chave in pessoa:
    print(chave, pessoa[chave])

print()
for chave, valor in aninhado.items():
    print(chave, valor)

print()
print(aninhado2["chave1"]["chave2.2"]["chave3.2"])

