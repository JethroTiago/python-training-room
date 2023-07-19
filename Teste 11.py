print('Cálculo de área')
print('')
largura = float(input('Qual a largura da parede (em metros)? '))
altura = float(input('Qual é a altura da parede (em metros)? '))
area = largura * altura
tinta = area / 2
print('Sua parede de {}m x {}m possui uma área de {}m², sendo necessário utilizar {:.2f} litros de tinta para pinta-la.'.format(largura, altura, area, tinta))
