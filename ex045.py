import time
import random
print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
jogadas = ['Pedra', 'Papel', 'Tesoura']
jc = random.choice(jogadas)
jogada = int(input('Qual é a sua jogada?'))
if jogada != 1 and jogada != 2 and jogada != 3:
    print('Você escolheu uma opção INVÁLIDA!!')
    quit()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
if jogada == 1:
    print('-=' * 15)
    print('Você escolheu Pedra')
    print('Computador escolheu {}'.format(jc))
    print('-=' * 15)
    if jc == 'Pedra':
        print('Empate!')
    elif jc == 'Papel':
        print('O computador venceu!')
    elif jc == 'Tesoura':
        print('Você venceu!')
elif jogada == 2:
    print('-=' * 15)
    print('Você escolheu Papel')
    print('Computador escolheu {}'.format(jc))
    print('-=' * 15)
    if jc == 'Pedra':
        print('Você venceu!!')
    elif jc == 'Papel':
        print('Empate!')
    elif jc == 'Tesoura':
        print('Computador venceu!')
elif jogada == 3:
    print('-=' * 15)
    print('Você escolheu Tesoura')
    print('Computador escolheu {}'.format(jc))
    print('-=' * 15)
    if jc == 'Pedra':
        print('Computador venceu!')
    elif jc == 'Papel':
        print('Você venceu!')
    elif jc == 'Tesoura':
        print('Empate!')