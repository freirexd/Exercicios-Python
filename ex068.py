import random
print('-='*15)
print('Vamos jogar Par ou Ímpar')
print('-='*15)
v = 0
while True:
    jogador = int(input('Diga um valor:'))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Ímpar [P/I]:')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'{total} é Par e você VENCEU!')
            v += 1
        else:
            print(f'{total} é Ímpar e você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'{total} é Ímpar e você VENCEU!')
            v += 1
        else:
            print(f'{total} é Par e você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!!!! Você venceu {v} vezes!')