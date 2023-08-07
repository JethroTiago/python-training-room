print('\033[1;34m-=-\033[m' * 15)
print('\033[1;35mDEZ TERMOS DE UMA PROGRESSÃO ARITMÉTICA\033[m')
print('\033[1;34m-=-\033[m' * 15)
termo = int(input('Digite o primeiro TERMO: '))
razao = int(input('Digite a RAZÃO: '))
decimo = termo + (11 - 1) * razao
for c in range(termo, decimo, razao):
    print('{}' .format(c), end =' => ')
print('FIM')
