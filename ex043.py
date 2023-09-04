print('\033[1;34mCalculadora de IMC (Índice de Massa Corporal)\033[m')
print('\033[1;32m-=-\033[m' * 20)
nome = str(input('Digite o nome do paciente: ')).strip()
altura = float(input('Digite a altura do paciente (m): '))
peso = float(input('Digite o peso do paciente (Kg): '))
imc = peso / (altura ** 2)
print('O \033[1:32mIMC\033[m do paciente \033[1:36m{}\033[m é de {:.1f}'.format(nome, imc))
if imc < 18.5:
    print('O paciente {} está \033[1:33mABAIXO DO PESO\033[m!'.format(nome))
elif imc < 25:
    print('O paciente {} está no \033[1:34mPESO IDEAL\033[m!'.format(nome))
elif imc < 30:
    print('O paciente {} está com \033[1:33mSOBREPESO\033[m!'.format(nome))
elif imc < 40:
    print('O paciente {} está com \033[1:31mOBESIDADE \033[m!'.format(nome))
else:
    print('O paciente {} está com \033[1:31mOBESIDADE MÓRBIDA\033[m!'.format(nome))
print('\033[1;32m-=-\033[m' * 20)
print('FIM')
'''IMC (adulto) - Ministério da saúde:
Abaixo de 18.5:  Abaixo do peso
Entre 18.5 e 25: Peso ideal
Entre 25 e 30:   Sobrepeso
Entre 30 e 40:   Obesidade
Acima de 40:     Obesidade Mórbida'''
