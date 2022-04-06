num = []
par = []
imp = []
for c in (range(1, 8)):
    v = int(input(f'Digite o {c}º valor: '))
    num.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print()
par.sort()
imp.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {imp}')