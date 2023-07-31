print('\033[1;31mConversor de bases númericas\033[m')
print('\033[1;34m-=-\033[m' * 25)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções abaixo para conversão:
[ \033[31m1\033[m ] Converter para BINÁRIO
[ \033[31m2\033[m ] Converter para OCTAL
[ \033[31m3\033[m ] Converter para HEXADECIMAL''')
opcao = int(input('Digite o \033[31mnúmero\033[m referente a opção escolhida: '))
print('A opção selecionada foi {}'.format(opcao))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)))
print('\033[1;34m-=-\033[m' * 25)
print('FIM')
