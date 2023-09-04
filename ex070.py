print('\033[1;36m-=-\033[m' * 15)
print('\033[1;31mESTATÍSTICAS EM PRODUTOS\033[m')
print('\033[1;36m-=-\033[m' * 15)
total = maismil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço R$: '))
    contador += 1
    total += preco
    if preco > 1000:
        maismil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total gasto nas compras foi de R$ {total}')
print(f'{maismil} produtos custaram mais de R$ 1000')
print(f'O produto mais barato foi {barato} e ele custou {menor:.2f}')
print('FIM')
