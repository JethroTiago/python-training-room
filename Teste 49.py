print('\033[1;37mTABUADA\033[m')
print('\033[1;34m-=-\033[m' * 24)
num = int(input('Digite um número para verificar a sua tabuada: '))
multip = 0
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('\033[1;34m-=-\033[m' * 24)
print('FIM')
