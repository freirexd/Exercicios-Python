tot = mais1000 = menor = cont = 0
barato = ' '
while True:
    product = str(input('Nome do produto:')).strip()
    price = float(input('Preço: R$'))
    cont += 1
    tot += price
    if price > 1000:
        mais1000 += 1
    '''if cont == 1 or price < menor:
        menor = price
        barato = product'''
    if cont == 1:
        menor = price
        barato = product
    else:
        if price < menor:
            menor = price
            barato = product
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('Fim do Programa!'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi ({barato}) que custa R${menor:.2f}')
