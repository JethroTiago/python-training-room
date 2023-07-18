print('Exercicios aritméticos')
print('')
n = int(input('Digite um número: '))
print('O número digitado foi: {}'.format(n))
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n, (n*3)))
print('A raiz quadrada de {} é {:.2f}'.format(n, (n**(1/2))))
# Também poderia ser atribuido variaveis para dobro, triplo e raíz quadrada
# O {:.2f} é uma parâmetro que limita a quantidade de caracteres após o ponto em 2
# pow(n, (1/2)) também calcula a raíz quadrada