print('Ano bissexto')
from datetime import date
print('-=-' * 27)
ano = int(input('Digite um ano para saber se ele é bissexto. Digite 0 para analisar o ano atual: '))
print('=-=' * 27)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:# <<< Código padrão para analisar anos bissextos
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
print('FIM')
