'''import math
print ('Descobrindo a porção inteira e importando math')
print('')
#1ª forma de fazer é com import math
valor = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(valor, math.trunc(valor)))'''

#2ª forma de fazer é com from math import trunc
from math import trunc
num = float(input('Digite mais um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

'''#3ª forma de fazer é não importando nada e utilizando o int
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))'''
