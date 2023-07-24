print('Analisando um número')
print('')
num = int(input('Digite um número (de 0 a 9999): '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))
