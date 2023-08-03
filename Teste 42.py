print('\033[1;33mAnalisador/Classificador de TRIÂNGULOS\033[m')
print('\033[1;31m-=-\033[m' * 25)
r1 = float(input('Digite o valor do PRIMEIRO segmento: '))
r2 = float(input('Digite o valor do SEGUNDO segmento: '))
r3 = float(input('Digite o valor do TERCEIRO segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos digitados podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[1:34mEQUILÁTERO\033[m!')
    elif r1 != r2 != r3 != r1:
        print('\033[1:34mESCALENO\033[m!')
    else:
        print('\033[1:34mISÓSCELES\033[m')
else:
    print('Os segmentos digitados \033[1;31mnão\033[m podem formar um triângulo!')
print('\033[1;31m-=-\033[m' * 25)
print('FIM')
'''TIPOS DE TRIÂNGULO
Triângulo EQUILÁTERO tem todos os lados iguais
Triângulo ESCALENO tem todos os lados diferentes
Triângulo ISÓSCELES tem dois lados iguais e um diferente'''
