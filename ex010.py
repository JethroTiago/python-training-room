print('Conversor de moeda')
print('')
real = float(input('Digite o valor (em Real) para conversão: R$ '))
dolar = real / 4.81
euro = real / 5.40
iene = real / 0.035
print('R$ {:.2f} = US$ {:.2f} (Dollár)'.format(real, dolar))
print('R$ {:.2f} = € {:.2f} (Euro)'.format(real, euro))
print('R$ {:.2f} = ¥ {:.2f} (Iene)'.format(real, iene))
# 4.81 é o valor do Dóllar americano em 07/2023
# 5.40 é o valor do Euro em 07/2023
# 0.035 é o valor do Iene Japonês em 07/2023
