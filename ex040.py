n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
print('Sua média é {}'.format(media))
if media < 5:
    print('Você foi \033[31mREPROVADO!!')
elif media >= 5 and media <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO!!')
elif media >= 7:
    print('Você foi \033[32mAPROVADO!!\033[m \033[4;97mPARABÉNS!!')

