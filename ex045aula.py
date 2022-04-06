import time
import random
print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
itens = ('Pedra', 'Papel', 'Tesoura')
jc = random.randint(1,3)
jogada = int(input('Qual é a sua jogada?'))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=' * 15)
print('Você escolheu {}'.format(itens[jogada]))
print('Computador escolheu {}'.format(itens[jc]))
print('-=' * 15)
if jogada == 1:
    if jc == 1:
        print('Empate!')
    elif jc == 2:
        print('O computador venceu!')
    elif jc == 3:
        print('Você venceu!')
elif jogada == 2:
    if jc == 1:
        print('Você venceu!!')
    elif jc == 2:
        print('Empate!')
    elif jc == 3:
        print('Computador venceu!')
elif jogada == 3:
    if jc == 1:
        print('Computador venceu!')
    elif jc == 2:
        print('Você venceu!')
    elif jc == 3:
        print('Empate!')
else:
    print('Você escolheu uma opção INVÁLIDA!!')