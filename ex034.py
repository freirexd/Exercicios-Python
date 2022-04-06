salario = float(input('Qual é o sálario do funcionário? R$'))
if salario >=1250:
    aumento = (salario / 100 * 10) + salario
else:
    aumento = (salario / 100 * 15) + salario
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))
