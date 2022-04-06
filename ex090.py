aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]} é: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-+' * 30)
print(f'- Nome: {aluno["nome"]}')
print(f'- Média: {aluno["media"]}')
print(f'- Situação: {aluno["situação"]}')