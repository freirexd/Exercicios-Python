listap = []
listai = []
lista = []
while True:
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    if n % 2 != 0:
        listai.append(n)
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listap}')
print(f'A lista de ímpares é {listai}')