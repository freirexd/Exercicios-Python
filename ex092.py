from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (use 0 se não tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Sálario: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print()
for k, v in dados.items():
    print(f'{k}: {v}')