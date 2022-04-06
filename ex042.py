print('-'*25)
print('Analisador de Triângulos')
print('-'*25)
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos podem formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('Equilátero!')
    elif s1 != s2 != s3 != s1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos não podem formar um triângulo!')

