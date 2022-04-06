times = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense',
         'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino',
         'Ceará', 'Corinthians', 'Atlético Goianiense', 'Bahia', 'Sport Recife',
         'Fortaleza', 'Vasco da gama', 'Goias', 'Coritiba', 'Botafogo')
print(f'Listas dos times do Brasileirão: {times}')
print('-=' * 160)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 160)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 160)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 160)
print(f'O Bahia está na {times.index("Bahia")+1}ª posição')