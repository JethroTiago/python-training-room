'''from math import factorial
numero = int(input('Digite um número para calcular o seu FATORIAL: '))
fatorial = factorial(n)
print('O FATORIAL de {} é {}.'.format(n, f))'''
print('\033[1;33m-=-\033[m' * 15)
print('\033[1;32mCALCULO DE FATORIAL\033[m')
print('\033[1;33m-=-\033[m' * 15)
# O método acima é mais simples, importando factorial from math
n = int(input('Digite um número para calcular o seu \033[1;32mFATORIAL\033[m: '))
c = n
f = 1
print('CALCULANDO \033[1;32m{}!\033[m = '.format(n), end='')
while c > 0:
    print('\033[1;32m{}\033[m'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
print('\033[1;33m-=-\033[m' * 15)
print('FIM')
