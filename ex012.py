print('Calculo de porcentagem')
print('')
valor = float(input('Qual é o valor do produto? R$'))
cinco = valor - (valor * 5 / 100)
dez = valor - (valor * 10 / 100)
print('Com desconto de 5%, o valor será R${}'.format(cinco))
print('Com desconto de 10%, o valor será R${}'.format(dez))
print('Boas compras!')
