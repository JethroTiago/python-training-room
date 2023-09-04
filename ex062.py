print('\033[1;34m-=-\033[m' * 15)
print('\033[1;31mSUPER PROGRESSÃO ARITMÉTICA\033[m')
print('\033[1;34m-=-\033[m' * 15)
primeiro = int(input('Digite o primeiro \033[1;35mTERMO\033[m: '))
razao = int(input('Digite a \033[1;36mRAZÃO\033[m: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} \033[1;32m->\033[m '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa.')
    mais = int(input('Digite quantos termos você quer mostrar a mais: '))
print('\033[1;34m-=-\033[m' * 15)
print('Progressão finalizada com {} \033[1;35mTERMOS\033[m exibidos.'.format(total))
print('\033[1;34m-=-\033[m' * 15)
print('FIM')
