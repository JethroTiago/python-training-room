print('Sorteio de nomes')
print('')
from random import shuffle
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
n5 = str(input('Digite o quinto nome: '))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
