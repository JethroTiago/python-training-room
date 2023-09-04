print('\033[1;34m-=-\033[m' * 15)
print('\033[1;35mMAIOR E MENOR DA SEQUÊNCIA\033[m')
print('\033[1;34m-=-\033[m' * 15)
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1: #O primeiro valor digitado
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
