from datetime import date
print('\033[1;31mAlistamento Militar\033[m')
print('\033[1;34m-=-\033[m' * 25)
print('Qual o sexo do candidato?')
nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
sexo = str(input('Digite "M" para MASCULINO ou "F" para FEMININO: ' ))
if idade == 18 and sexo == 'M':
    print('O candidato tem 18 anos e deve realizar o ALISTAMENTO neste ano!')
elif idade < 18 and sexo == 'M':
    saldo = 18 - idade
    ano = atual + saldo
    print('Ainda faltam {} anos para o candidato realizar o alistamento.'.format(saldo))
    print('O seu alistamento será no ano de {}.'.format(ano))
elif idade > 18 and sexo == 'M':
    saldo = idade - 18
    ano = atual - saldo
    print('O candidato deveria ter se alistado há {} anos.'.format(saldo))
    print('O ano de seu alistamento foi {}.'.format(ano))
elif sexo == 'F':
    print('O alistamento para mulheres não é obrigatório.')
else:
    print('O valor digitado está incorreto. Tente novamente.')