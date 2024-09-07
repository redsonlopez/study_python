print("Parte I")
def calcular_desconto(valor, desconto=0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100)
valor2 = calcular_desconto(100, 0.25)

print(f"Primeiro valor a ser pago = {valor1}")
print(f"Segundo valor a ser pago = {valor2}")

print("\nParte II")
def converter_minuscula(texto, flag_minuscula=True):
    if flag_minuscula:
        return texto.lower()
    else:
        return texto.upper()

texto1 = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de Programação")
texto2 = converter_minuscula(texto="LINGUAGEM de Programação")

print(f"Texto 1 = {texto1}")
print(f"Texto 2 = {texto2}")

print("\nParte III")
def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

imprimir_parametros("São Paulo", "João", 23)

print("\nParte IV")
def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

