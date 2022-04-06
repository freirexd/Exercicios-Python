value1 = float(input('Digite o 1º valor:'))
value2 = float(input('Digite o 2º valor:'))
terminar = False
while not terminar:
    choice = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
>>> Escolha uma opção:'''))
    if choice == 1:
        addition = value1 + value2
        print('A soma entre {} e {} é {}'.format(value1, value2, addition))
    elif choice == 2:
        multiplication = value1 * value2
        print('O resultado de {} x {} é {}'.format(value1, value2, multiplication))
    elif choice == 3:
        if value1 > value2:
            print('Entre {} e {} o maior valor é {}'.format(value1, value2, value1))
        elif value1 < value2:
            print('Entre {} e {} o maior valor é {}'.format(value1, value2, value2))
        elif value1 == value2:
            print('Os dois valores são iguais.')
    elif choice == 4:
        print('Informe outros valores!')
        value1 = float(input('1º valor:'))
        value2 = float(input('2º valor:'))
    elif choice == 5:
        terminar = True
    else:
        print('Opção invalida! Tente novamente')
print('Fim do programa! Volte sempre!')