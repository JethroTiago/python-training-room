print('\033[1;31mComparador de números\033[m')
print('\033[1;34m-=-\033[m' * 25)
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro valor digitado é MAIOR.')
elif num1 < num2:
    print('O segundo valor digitado é MAIOR.')
else:
    print('Os números digitados são iguais!')
