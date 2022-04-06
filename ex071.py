saque = int(input('Que valor você quer sacar? R$'))
total = saque
notas = 50
totalnotas = 0
while True:
    if total >= notas:
        total -= notas
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} cédulas de R${notas}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalnotas = 0
        if total == 0:
            break
