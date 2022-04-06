def maior(*num):
    if len(num) > 0:
        cont = 0
        print('=' *50)
        print('Analisando os valores passados...')
        for valor in num:
            print(f'{valor} ', end='')
            cont += 1
        print(f'Foram informados {cont} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print('=' * 50)
        print('Não foi informado nenhum valor!')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
