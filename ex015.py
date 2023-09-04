print('Aluguel de carro')
print('')
dias = int(input('Por quantos dias o carro foi alugado? '))
kms = float(input('Quantos Kms foram rodados? '))
valor = dias * 60 + kms * 0.15
print('O valor a ser pago é de R${:.2f}'.format(valor))
