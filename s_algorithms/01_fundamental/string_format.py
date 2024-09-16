PI= 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")
print()

profissao= "Programador"
nome= "Hedson"
altura= 1.70
idade= 37
dados= {"name": "Hedson", "age": 37, "job": "Programador"}

print("Nome: %s, Idade: %d, Altura: %f Profissão: %s" % (nome, idade, altura, profissao))
print("Nome: {}, Idade: {}, Altura: {:.2f}, Profissão: {}".format(nome, idade, altura, profissao))
print("Profissão: {3}, Nome: {0}, Idade: {1}, Altura: {2:.2f}".format(nome, idade, altura, profissao))
print("Nome: {name}, Profissão: {job}".format(job= profissao, name= nome))
print("Profissão: {job}, Nome: {name}, Idade: {age}".format(**dados))
print(f"Nome: {nome}, Altura: {altura:10.2f}")

