def dados(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gols(s) no campeonato.')


# Main
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    dados(gol=g)
else:
    dados(n, g)
