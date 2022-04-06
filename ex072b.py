num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    nd = int(input('Digite um número entre 0 e 20: '))
    if 0 <= nd <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num[nd]}')
continuar = ''
while True:
    continuar = str(input('Gostaria de escolher outro número? [S/N]')).strip().upper()[0]
    if continuar == 'S':
        while True:
            nd = int(input('Digite um número entre 0 e 20: '))
            if 0 <= nd <= 20:
                break
            print('Tente novamente. ', end='')
        print(f'Você digitou o número {num[nd]}')
    if continuar == 'N':
        break
    if continuar not in 'SN':
        print('Error!')
print('Obrigado! Volte sempre!')