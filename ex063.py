print('\033[1;34m-=-\033[m' * 15)
print('\033[1;33mSEQUÊNCIA DE FIBONACCI V1.0\033[m')
print('\033[1;34m-=-\033[m' * 15)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} --> {} '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('--> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('--> FIM')
print('\033[1;34m-=-\033[m' * 15)
