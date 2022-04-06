peso = float(input('Qual é o seu peso (kg):'))
altura = float(input('Qual é a sua altura (m):'))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f} e seu status é: '.format(imc), end='')
if imc < 18.5:
    print('\033[31mAbaixo do peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mPeso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[31mObesidade!\033[m')
else:
    print('\033[30mObesidade mórbida!\033[m')
