print('\033[1;33m-=-\033[m' * 15)
print('\033[1;34mNÚMEROS PRIMOS\033[m')
print('\033[1;34m-=-\033[m' * 15)
num = int(input('Digite um número para ser analisado: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('O número {} é um número \033[1;35mPRIMO\033[m.'.format(num))
else:
    print('O número {} \033[1;31mnão\033[m é um número \033[1;35mPRIMO\033[m.'.format(num))
print('\033[1;34m-=-\033[m' * 15)
print('FIM')
