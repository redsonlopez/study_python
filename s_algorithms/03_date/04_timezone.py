from datetime import datetime, timezone, timedelta

data_oslo= datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo= datetime.now(timezone(timedelta(hours=-3)))
print(f"{data_oslo}\n{data_sao_paulo}")

