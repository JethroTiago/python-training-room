from random import randint
from time import sleep
print('\033[1;34mJogo de JOKENPO\033[m')
print('{:=^80}'.format(' \033[1;31mJO\033[m\033[1;32mKEN\033[m\033[1:34mPO\033[m '))
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''ESCOLHA SUA OPÇÃO:
[ \033[1;31m0\033[m ] \033[1;31mPEDRA\033[m
[ \033[1;32m1\033[m ] \033[1;32mPAPEL\033[m
[ \033[1:34m2\033[m ] \033[1:34mTESOURA\033[m''')
jogador = int(input('Digite sua escolha: '))
print('\033[1;31mJO\033[m')
sleep(0.5)
print('\033[1;32mKEN\033[m')
sleep(0.5)
print('\033[1:34mPO\033[m!!!')
sleep(0.5)
print('\033[1:36m=-=\033[m' * 10)
print('O computador escolheu {}.'.format(opcoes[computador]))
print('Você escolheu {}.'.format(opcoes[jogador]))
print('\033[1:36m=-=\033[m' * 10)
if computador == 0: #Se o computador escolheu PEDRA
    if jogador == 0:
        print('\033[1:34mEMPATE!!!\033[m')
    elif jogador == 1:
        print('\033[1:32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[1:33mCOMPUTADOR VENCEU!!!\033[m')
    else:
        print('\033[1:31mJOGADA INVÁLIDA!\033[m')
elif computador == 1: #Se o computador escolheu PAPEL
    if jogador == 0:
        print('\033[1:33mCOMPUTADOR VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[1:34mEMPATE!!!\033[m')
    elif jogador == 2:
        print('\033[1:32mVOCÊ VENCEU!!!\033[m')
    else:
        print('\033[1:31mJOGADA INVÁLIDA!\033[m')
elif computador == 2: #Se o computador escolheu TESOURA
    if jogador == 0:
        print('\033[1:32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[1:33mCOMPUTADOR VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[1:34mEMPATE!!!\033[m')
    else:
        print('\033[1:31mJOGADA INVÁLIDA!\033[m')
print('\033[1:37m=-=\033[m' * 10)
print('FIM')
