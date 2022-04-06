'''oposto = float(input('Comprimento do cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format (hipotenusa))'''

from math import hypot
oposto = float(input('Comprimento do cateto oposto:'))
adjacente = float(input('Comprimento do cateto adjacente:'))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))