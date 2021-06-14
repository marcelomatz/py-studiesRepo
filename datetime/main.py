from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

# data = datetime(2021, 5, 30, 20, 8, 20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))
setlocale(LC_ALL, 'pt_BR.utf-8')
d1 = datetime.strptime('27/04/1984 06:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('27/04/1985 20:20:00', '%d/%m/%Y %H:%M:%S')
diff = d2 - d1
print(diff)

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
nome_mes_atual = dt.strftime('%B')
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

print(nome_mes_atual, mes_atual, mdays[mes_atual])
