print('Custo de viagem')
print('')
distancia = float(input('Qual é a distância de sua viagem: '))
print('Você está prestes a começar uma viagem de {}kms'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
'''preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45'''
print('O preço de sua passagem será de R${:.2f}'.format(preco))
print('Faça uma boa viagem!')
