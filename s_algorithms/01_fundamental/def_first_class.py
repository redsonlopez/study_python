PI= 3.14159

def somar(a, b):
    return a + b

def subitrair(a, b):
    return a - b

def circunferencia(raio, lista):
    global PI
    lista_auxiliar= lista.copy()
    lista_auxiliar.append(2)
    print(lista)
    print(lista_auxiliar)
    c= 2 * PI * raio
    return f"{c:.2f}"

def exibir_resultado(a, b, funcao):
    resultado= funcao(a, b)
    print(f"O resultado da operação é {resultado}")

lista= [1]
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subitrair)

op= somar
print(op(5, 5))
print(circunferencia(144, lista))

