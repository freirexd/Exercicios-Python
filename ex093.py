jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {g+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-'* 40)
print(jogador)
print('-'* 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'* 40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na {i+1}º partida fez {v} gols.')
print(f'Fez ao total {jogador["total"]} gols.')