def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


print(' Controle de Terrenos ')
print('-' * 22)
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
