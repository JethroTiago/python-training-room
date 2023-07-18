print('Exercicios aritméticos')
print('')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divi = n1 / n2
print('A soma dos dois números digitados é {}'.format(soma), end=' e ')
print('a subtração dos valores é {}'.format(sub))
print('A multiplicação dos números é {}'.format(multi), end=' e ')
print('a divisão dos números digitados é {}'.format(divi))
n3 = int(input("Digite mais um número "))
ant = n3 - 1
pro = n3 + 1
print('O número que antecede o valor digitado é {}'.format(ant))
print('O número que sucede o valor digitado é {}'.format(pro))
#Testando com menos váriaveis:
print('O número digitado foi {} e o número que o antecede é {} e o que sucede é {}'.format(n3, (n3-1), (n3+1)))
