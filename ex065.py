resp = 'S'
soma = 0
media = 0
quant = 0
maior = 0
menor = 0
# soma = media = quant = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número:'))
    soma = soma + n
    quant = quant + 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} número e a média é {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
