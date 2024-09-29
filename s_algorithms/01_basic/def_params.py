# def f(positional only, /, positional or keyword, *, keyword only)
def criar_carro(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

carro= criar_carro("Palio", 1999, "ABC-1234", marca= "Fiat", motor= "1.0", combustivel= "Gasolina")
print(carro)

