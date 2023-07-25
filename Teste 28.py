from random import randint
from time import sleep
computador = randint (1, 5)
print('-=-' * 27)
print('O computador pensou em um número entre 1 e 5. Você consegue adivinhar qual foi?')
print('=-=' * 27)
jogador = int(input('Digite um número entre 1 e 5: '))
sleep(3)
if jogador == computador:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! O computador pensou no número {}'.format(computador))
print('FIM')