num = list()
while True:
    n = (int(input('Digite um valor:')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
num.sort()
print(f'Você digitou os valores {num}')