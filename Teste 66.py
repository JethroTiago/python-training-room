print('\033[1;35m-=-\033[m' * 15)
print('\033[1;34mVÁRIOS NÚMEROS COM FLAG\033[m')
print('\033[1;35m-=-\033[m' * 15)
contador = soma = 0
while True:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} números e a soma deles é {soma}.')
print('FIM')
#999 é o FLAG e ele não entra na soma graças ao BREAK
