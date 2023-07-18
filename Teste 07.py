print('Obtendo uma média')
print('')
aluno = input('Por favor, digite o nome do aluno: ')
print('Seja bem vindo {}. Vamos agora obter a sua média'.format(aluno))
teste = float(input('>>> Qual foi a sua nota no teste? '))
prova = float(input('>>> Qual foi a sua nota na prova? '))
media = (teste + prova)/2
print('>>> {}, a sua média do foi: {:.1f}'.format(aluno, media))
# O {:.1f} significa que apenas um número decimal aparecerá após o ponto flutuante
