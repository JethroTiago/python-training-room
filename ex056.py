print('\033[1;34m-=-\033[m' * 15)
print('\033[1;35mANALISADOR COMPLETO\033[m')
print('\033[1;34m-=-\033[m' * 15)
maioridadehomem = 0
nomemaisvelho = ''
mulhermenor20 = 0
for pessoa in range(1, 5):
    print('----- {}ª pessoa -----'.format(pessoa))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    mediaidade = (idade * 4) / 4
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomemaisvelho))
print('{} são mulheres com menos de 20 anos'.format(mulhermenor20))
