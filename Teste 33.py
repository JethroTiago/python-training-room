from time import sleep
print('Encontrando o maior e o menor valor')
print('-=-' * 25)
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
valor3 = int(input('Digite o terceiro número: '))
print('PROCESSANDO...')
sleep(2)
#Teste de verificação de qual é o menor valor:
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
print('O menor valor digitado foi o {}.'.format(menor))
#Teste de verificação de qual é o maior valor:
maior = valor3
if valor1 > valor3 and valor1 > valor2:
    maior = valor1
if valor2 > valor3 and valor2 > valor1:
    maior = valor2
print('O maior valor digitado foi o {}.'.format(maior))
print('FIM')
