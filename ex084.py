lista = []
pessoas = []
pesadas = leves = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesadas = leves = pessoas[1]
    else:
        if pessoas[1] > pesadas:
            pesadas = pessoas[1]
        if pessoas[1] < leves:
            leves = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {pesadas}Kg. Peso de: ', end='')
for p in lista:
    if p[1] == pesadas:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {leves}Kg. Peso de: ', end='')
for p in lista:
    if p[1] == leves:
        print(f'[{p[0]}] ', end='')
print()

