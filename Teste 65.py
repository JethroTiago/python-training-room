print('\033[1;35m-=-\033[m' * 15)
print('\033[1;34mMAIOR E MENOR VALOR\033[m')
print('\033[1;35m-=-\033[m' * 15)
resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('\033[1mQuer continuar\033[m [\033[1;36mS\033[m/\033[1;36mN\033[m]: ')).strip().upper()[0]
media = soma / quantidade
print('Você digitou \033[1;36m{}\033[m números e a \033[1;34mMÉDIA\033[m entre eles foi \033[1;36m{:.2f}\033[m.'.format(quantidade, media))
print('O \033[1;35mMAIOR\033[m valor digitado foi \033[1;36m{}\033[m e o \033[1;34mMENOR\033[m valor digitado foi \033[1;36m{}\033[m'.format(maior, menor))
