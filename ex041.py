import datetime

nasc = int(input('Nascimento do atleta:'))
idade = datetime.date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
print('Categoria: ', end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
