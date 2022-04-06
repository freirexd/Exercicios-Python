lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if r in 'N':
        break
print(f'\nVocê digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 NÃO faz parte da lista!')