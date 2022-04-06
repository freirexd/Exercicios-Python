import random
computador = random.randint(0, 10)
count = 1
print('Estou pensando em um número entre 0 e 10. Você consegue adivinhar?')
jogador = int(input('Digite o seu palpite:'))
while jogador != computador:
    jogador = int(input('Você errou, tente novamente:'))
    count += 1
print('Parabéns, você acertou com {} palpites!'.format(count))