from time import sleep
print('Aumentos múltiplos - porcentagem')
print('-=-' * 25)
salario = float(input('Digite o salário do funcionário: R$ '))
print('Calculando...')
sleep(3)
aumento = 0
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('O novo salário do funcionário será de R${:.2f} (10% de aumento)'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('O novo salário do funcionário será de R${:.2f} (15% de aumento)'.format(aumento))
print('FIM')
