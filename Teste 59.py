from time import sleep
print('\033[1;34m-=-\033[m' * 15)
print('\033[1;33mMENU DE OPÇÕES\033[m')
print('\033[1;34m-=-\033[m' * 15)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''    [ \033[1;36m1\033[m ] \033[1mSOMAR\033[m
    [ \033[1;36m2\033[m ] \033[1mMULTIPLICAR\033[m
    [ \033[1;36m3\033[m ] \033[1mMAIOR\033[m
    [ \033[1;36m4\033[m ] \033[1mNOVOS NÚMEROS\033[m
    [ \033[1;36m5\033[m ] \033[1mSAIR DO PROGRAMA\033[m''')
    opcao = int(input('>>>>> ESCOLHA SUA OPÇÃO: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print('{} x {} é {}'.format(n1, n2, multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o \033[1;34mMAIOR\033[m valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('\033[1mINFORME OS VALORES NOVAMENTE:\033[m')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('\033[1mFINALIZANDO...\033[m')
        sleep(2)
    else:
        print('\033[1;31mOPÇÃO INVÁLIDA! DIGITE UM VALOR ENTRE 1 E 5.\033[m')
    print('\033[1;34m-=-\033[m' * 15)
print('\033[1;32mPROGRAMA FINALIZADO. VOLTE SEMPRE!\033[m')
