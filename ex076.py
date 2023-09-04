print('\033[1;34m=-=\033[m' * 15)
print('\033[1;33mLISTA DE PREÇOS COM TUPLAS\033[m')
print('\033[1;34m=-=\033[m' * 15)
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Caneta', 22.30,
         'Livro', 34.90
         )
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('\033[1;34m=-=\033[m' * 15)
for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>7.2f}')
print('\033[1;34m=-=\033[m' * 15)
print('FIM')
