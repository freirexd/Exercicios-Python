print('10 Termos de um P.A')
termo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' → ')
print('Acabou')