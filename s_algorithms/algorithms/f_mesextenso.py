def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'

data_entrada = input("Digite a data no formato DD/MM/AAAA: ")
print(converter_mes_para_extenso(data_entrada))

