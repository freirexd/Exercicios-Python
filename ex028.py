import random
import time

computador = random.randint(0, 5) #faz o computador "SORTEAR"
print('-' * 52)
print('Vou escolher um número de 0 a 5. Tende adivinhar...')
print('-' * 52)

jogador = int(input('Qual número eu escolhi?')) #Jogador tenta adivinhar
print('Processando...')
time.sleep(3)
if computador == jogador:
    print('Parabéns, você acertou o número que eu escolhi!')
else:
    print('Eu escolhi o numero {}, tente novamente!'.format(computador))
