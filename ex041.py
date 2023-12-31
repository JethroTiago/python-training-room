from datetime import date
print('\033[1;33mClassificação de Atletas\033[m')
print('\033[1;31m-=-\033[m' * 25)
ano = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem \033[1:32m{}\033[m anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[1:34mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[1:34mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[1:34mJÚNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[1:34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1:34mMASTER\033[m')
print('\033[1;31m-=-\033[m' * 25)
print('FIM')
