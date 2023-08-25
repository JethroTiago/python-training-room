print('\033[1;34m=-=\033[m' * 15)
print('\033[1;33mANALISE DE DADOS EM UMA TUPLA\033[m')
print('\033[1;34m=-=\033[m' * 15)
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('\033[1;34m=-=\033[m' * 15)
print(f'Você digitou os valores \033[1;33m{num}\033[m')
print('\033[1;34m=-=\033[m' * 15)
if 9 in num:
    print(f'O valor 9 foi digitado {num.count(9)} vezes.')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in num:
    print(f'O número 3 foi o digitado na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os valores \033[1;35mPARES\033[m foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print('\n')
print('\033[1;34m=-=\033[m' * 15)
print('FIM')