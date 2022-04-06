num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

#nd = int(input('Digite um número entre 0 e 20: '))
#while True:
#    if 0 <= nd <= 20:
#        print(f'Você digitou o número {num[nd]}')
#        break
#    else:
#        nd = int(input('Tente novamente. Digite um número entre 0 e 20: '))

while True:
    nd = int(input('Digite um número entre 0 e 20: '))
    if 0 <= nd <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num[nd]}')

