from random import randint
from time import sleep
from operator import itemgetter
jogo = {'1°Jogador': randint(1, 6),
        '2°Jogador': randint(1, 6),
        '3°Jogador': randint(1, 6),
        '4°Jogador': randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-+' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)