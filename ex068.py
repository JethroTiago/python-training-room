from random import randint
print('\033[1;36m-=-\033[m' * 15)
print('\033[1;31mJOGO DO PAR OU ÍMPAR\033[m')
print('\033[1;36m-=-\033[m' * 15)
print('Vamos jogar PAR ou ÍMPAR!')
print('=-=' * 15)
vitoria = 0
while True:
    player = int(input('ENTER YOUR NUMBER: '))
    computer = randint(0, 10)
    total = player + computer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {computer}. O TOTAL foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(f'-> {total} é PAR! Você Ganhou!')
            vitoria += 1
        else:
            print(f'-> {total} é ÍMPAR! Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'-> {total} é ÍMPAR! Você Ganhou!')
            vitoria += 1
        else:
            print(f'-> {total} é PAR! Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes!')
