print('\033[1;34m=-=\033[m' * 15)
print('\033[1;33mMAIOR E MENOR VALOR COM TUPLA\033[m')
print('\033[1;34m=-=\033[m' * 15)
from random import randint
numeros = (randint(1, 99), randint(1, 99), randint(1, 99),
     randint(1, 99), randint(1, 99), randint(1, 99))
print('\033[1;33mOs números sorteados foram:\033[m ', end='')
for n in numeros:
    print(f'/ \033[1;36m{n}\033[m / ', end='')
print(f'\nO \033[1;34mMAIOR\033[m valor sorteado foi \033[1;36m{max(numeros)}\033[m')
print(f'O \033[1;35mMENOR\033[m valor sorteado foi \033[1;36m{min(numeros)}\033[m')
#print(f'Eu sorteei os valores {numeros}')
