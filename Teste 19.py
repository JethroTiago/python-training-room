print('Sorteio de nomes')
print('')
import random
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
nome5 = str(input('Digite o quinto nome: '))
lista = [nome1, nome2, nome3, nome4, nome5]
sorteado = random.choice(lista)
print('O nome sorteado foi {}'.format(sorteado))
