num = int(input('Digite um número inteiro:'))
conversor = int(input('''Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal
Sua opção:'''))
if conversor == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif conversor == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif conversor == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[0;31mERROR!!\033[m Tente novamente.')