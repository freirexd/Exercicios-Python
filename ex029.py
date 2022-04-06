v = float(input('Qual é a velocidade atual do carro?'))
m = (v - 80) * 7
if v >80:
    print('MULTADO! Você ultrapassou o  limite de velocidade que é 80Km/h.')
    print('Você deve pagar uma multa de R${:.2f}'.format(m))
print('Você está dentro do limite. Tenha um boa dia!')
