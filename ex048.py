print('\033[1;36mSoma ímpares multiplos de 3\033[m')
print('\033[1;33m-=-\033[m' * 24)
cont = 0
soma = 0
for c in range (3, 501, 2):
    if c % 3 == 0:
        cont += 1 #contador (cont = cont + 1)
        soma += c #acumulador (soma = soma + c
        print(c)
print('\033[1;33m-=-\033[m' * 24)
print('A soma dos {} valores acima é {}.'.format(cont, soma))
