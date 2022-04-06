c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor:'))
    print('='*40)
    if n < 0:
        break
    c += 1
    for c in range(1,11):
        print(f'{n} x {c:2} = {n*c}')
    print('='*40)
print('Programa finalizado! Volte sempre :) ')