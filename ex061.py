print('      Gerador de P.A')
print('-*'*13)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da P.A:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} --> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('Fim')