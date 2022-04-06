print('-'*20)
print('Cadastre uma pessoa')
print('-'*20)
mais18 = homens = mulheres20 = 0
while True:
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]:')).strip().upper()[0]
    if i >= 18:
        mais18 += 1
    if s == 'M':
        homens += 1
    if s == 'F' and i < 20:
        mulheres20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]?')).strip().upper()[0]
        print('-'*30)
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao menos temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
