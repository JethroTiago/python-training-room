print('\033[1;35m-=-\033[m' * 15)
print('\033[1;32mNÚMERO POR EXTENSO\033[m')
print('\033[1;35m-=-\033[m' * 15)
cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
        'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
        'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
        'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número \033[1;32m{cont[num]}\033[m.')
        resposta = ' '
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if resposta == 'N':
                break
    else:
        print('Número inválido. ', end='')
print('\033[1;35m-=-\033[m' * 15)
print('\033[1mPROGRAMA FINALIZADO!\033[m')
