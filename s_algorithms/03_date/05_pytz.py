import pytz
from datetime import datetime

data_1= datetime.now(pytz.timezone("Europe/Oslo"))
data_2= datetime.now(pytz.timezone("America/Sao_Paulo"))
print(f"{data_1}\n{data_2}")

