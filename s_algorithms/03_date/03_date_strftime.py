from datetime import datetime

# Formatando data e hora
d= datetime.now()
print(d.strftime("%d/%m/%Y %H:%M"))
print(d.strftime("%a dia %d de %b de %Y"))
print()

# Convertendo string para datatime
data_string= "16/10/2024 13:30"
d= datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(d)

