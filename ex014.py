print('Conversor de temperatura')
print('')
celsius = float(input('Digite a temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32
print('A temperatura de \033[4;35m{}ºC\033[m equivale a {}ºF.'.format(celsius, fahrenheit))
