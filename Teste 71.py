from time import sleep
print('\033[1;36m-=-\033[m' * 15)
print('\033[1;31mSIMULADOR DE CAIXA ELETRÔNICO\033[m')
print('\033[1;36m-=-\033[m' * 15)
print('==' * 30)
print('{:^60}'.format('\033[1mBANCO PYTHON\033[m'))
print('==' * 30)
print('\033[1;31mNOTAS DE\033[m \033[1;32mR$50\033[m, \033[1;32mR$20\033[m, \033[1;32mR$10\033[m \033[1;31mE\033[m \033[1;32mR$1\033[m \033[1;31mDISPONÍVEIS\033[m')
valor = int(input('Digite o valor do saque: R$ '))
total = valor
cedula = 50
totalcedulas = 0
print('\033[1mCONTANDO CÉDULAS...\033[m')
sleep(2)
while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Saque total de {totalcedulas} cédulas de \033[1;32mR${cedula}\033[m')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break
print('==' * 30)
print('{:^60}'.format('\033[1mVOLTE SEMPRE\033[m'))
print('FIM')
