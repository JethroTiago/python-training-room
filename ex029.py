print('Radar de velocidade e multa')
print('')
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('A velocidade excedeu o limite permitido.')
    print('O condutor deverá pagar multa de R${}'.format(multa))
print('Tudo em ordem. O condutor pode seguir viagem.')
