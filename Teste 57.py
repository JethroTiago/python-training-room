print('\033[1;34m-=-\033[m' * 15)
print('\033[1;33mANALISADOR DE SEXO\033[m')
print('\033[1;34m-=-\033[m' * 15)
sexo = str(input('Digite o seu sexo [\033[1;32mM\033[m/\033[1;36mF\033[m]: ')).strip().upper()[0] #o 0 pega a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Por favor, Digite \033[1;32mM\033[m para \033[1;32mMasculino\033[m ou \033[1;36mF\033[m para \033[1;36mFeminino\033[m: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo \033[1;32mMASCULINO\033[m registrado com sucesso.')
else:
    print('Sexo \033[1;36mFEMININO\033[m registrado com sucesso.')
print('\033[1;34m-=-\033[m' * 15)
print('FIM')
