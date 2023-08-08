from datetime import date
print('\033[1;33m-=-\033[m' * 15)
print('\033[1;35mMAIOR/MENOR DE IDADE\033[m')
print('\033[1;33m-=-\033[m' * 15)
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Digite o ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade = atual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo, tivemos {} pessoas \033[1;35mMAIORES\033[m de idade e {} pessoas \033[1;35mMENORES\033[m.'.format(totalmaior, totalmenor))
print('\033[1;33m-=-\033[m' * 15)
print('\033[1;35mFIM\033[m')
