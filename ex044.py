produto = float(input('Valor do produto:'))
print('''Formas de Pagamento
[1] à vista dinheiro/cheque (10% de desconto)
[2] à vista no cartão (5% de desconto)
[3] 2x no cartão (sem juros)
[4] 3x ou mais no cartão (20% de juros)''')
pagamento = float(input('Escolha a forma de pagamento:'))
p1 = produto - (produto / 100 * 10)
p2 = produto - (produto / 100 * 5)
p3 = produto / 2
p4 = produto + (produto / 100 * 20)
if pagamento == 1:
    print('Sua compra de R${:.2f} irá custar R${:.2f}'.format(produto, p1))
elif pagamento == 2:
    print('Sua compra de R${:.2f} irá custar R${:.2f}'.format(produto, p2))
elif pagamento == 3:
    print('Sua compra irá custar R${:.2f} em 2 parcelas de R${:.2f} sem juros.'.format(produto, p3))
elif pagamento == 4:
    parcelas = int(input('Gostaria de parcelar em quantas vezes?'))
    px = p4 / parcelas
    print('Sua compra de R${:.2f} irá custar R${:.2f} em {} parcelas de R${:.2f}'.format(produto, p4, parcelas, px))
else:
    print('Opção inválida! Tente novamente.')
