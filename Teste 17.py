print('Cateto e hipotenusa')
print('')
#Utilizando formula matemática padrão
opo = float(input('Qual é o comprimento do cateto oposto? '))
adj = float(input('Qual é o comprimento do cateto adjacente? '))
hipo = (opo ** 2 + adj ** 2) ** (1/2)
print('A hipotenusa terá {:.2f} de comprimento.'.format(hipo))
