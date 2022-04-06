import datetime
nasceu = int(input('Ano de nascimento:'))
idade = datetime.date.today().year - nasceu
print('Quem nasceu em {} terá {} anos em {}.'.format(nasceu, idade, datetime.date.today().year))
if idade == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = datetime.date.today().year + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = datetime.date.today().year - saldo
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano))