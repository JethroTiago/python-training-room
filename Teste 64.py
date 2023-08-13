print('\033[1;34m-=-\033[m' * 15)
print('\033[1;33mTRATANDO VÁRIOS VALORES V1.0\033[m')
print('\033[1;34m-=-\033[m' * 15)
n = cont = soma = 0
n = int(input('Digite um número [digite 999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [digite 999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
print('FIM')
