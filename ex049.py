num = int(input('Digite um número para ver sua tabuada:'))
for tab in range(1, 11):
    print('{} x {:2} = {}'.format(num, tab, num*tab))
