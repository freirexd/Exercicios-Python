dist = float(input('Qual a distância da sua viagem?'))
import time
print('Processando...')
time.sleep(1)
if dist <=200:
    price = dist * 0.50
else:
    price = dist * 0.45
print('A passagem custará R${:.2f}'.format(price))

