print('\033[1;34m-=-\033[m' * 15)
print('\033[1;35mPROGRESSÃO ARITMÉTICA V2.0\033[m')
print('\033[1;34m-=-\033[m' * 15)
primeiro = int(input('Digite o primeiro \033[1;35mTERMO\033[m: '))
razao = int(input('Digite a \033[1;36mRAZÃO\033[m: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} \033[1;31m->\033[m '.format(termo), end='')
    termo += razao
    contador += 1
print('\033[1;31mFIM\033[m')
print('\033[1;34m-=-\033[m' * 15)
