print('\033[1;36m-=-\033[m' * 15)
print('\033[1;31mANÁLISE DE DADOS DE UM GRUPO\033[m')
print('\033[1;36m-=-\033[m' * 15)
total18 = homenstotal = mulherestotal = 0
while True:
    idade = int(input('\033[1mDigite a idade do cliente:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1mDigite o sexo do cliente [M\F]\033[m: ')).upper().strip()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homenstotal += 1
    if sexo == 'F' and idade < 20:
        mulherestotal += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('\033[1mContinuar? [S/N]:\033[m ')).upper().strip()[0]
    if resposta == 'N':
            break
print('\033[1;36m-=-\033[m' * 15)
print(f'Cadastrado \033[1;31m{total18} pessoas\033[m com 18 anos ou mais.')
print(f'Foram cadastrados \033[1;31m{homenstotal} pessoas\033[m do sexo masculino.')
print(f'Foram cadastradas \033[1;31m{mulherestotal} mulheres\033[m com menos de 20 anos.')
