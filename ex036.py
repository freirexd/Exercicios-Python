print('A parcela mensal não pode exceder 30% do seu sálario!')
casa = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento:'))
prestacao = casa / (anos * 12)
minimo = salario / 100 * 30
print('Para pagar uma casa de RS{:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
