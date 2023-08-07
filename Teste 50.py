print('\033[1;36mSoma dos números pares inseridos\033[m')
print('\033[1;35m-=-\033[m' * 24)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números \033[1;32mPARES\033[m e a soma deles é: \033[1;32m{}\033[m.'.format(cont, soma))
print('\033[1;35m-=-\033[m' * 24)
print('FIM')
