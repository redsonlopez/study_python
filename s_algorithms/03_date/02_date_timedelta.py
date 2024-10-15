from datetime import datetime, timedelta

d= datetime(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

d= d + timedelta(weeks=1)
print(d)

resultado= d - timedelta(hours= 1)
print(resultado.time())

print(datetime.now().date())
print()

##
# Sistema para Lava-Jato
##

tipo_carro= "P" # P, M, G
tempo_pequeno= 30
tempo_medio= 45
tempo_grande= 60
data_atual= datetime.now()

if tipo_carro == "P":
    data_estimada= data_atual + timedelta(minutes= tempo_pequeno)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

elif tipo_carro == "M":
    data_estimada= data_atual + timedelta(minutes= tempo_medio)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

else:
    data_estimada= data_atual + timedelta(minutes= tempo_grande)
    print(f"O carro chegou às {data_atual} e ficará pronto às {data_estimada}")

