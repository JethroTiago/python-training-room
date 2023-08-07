print('\033[1;36mSoma dos números pares inseridos\033[m')
print('\033[1;35m-=-\033[m' * 24)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números PARES e a soma deles é: {}.'.format(cont, soma))
