print('\033[1;34m-=-\033[m' * 15)
print('\033[1;33mJOGO DE ADIVINHAÇÃO MELHORADO\033[m')
print('\033[1;34m-=-\033[m' * 15)
from random import randint
computador = randint(0, 10)
print('''\033[1mOLÁ! SOU SEU COMPUTADOR...
Acabei de pensar em um número entre \033[1;36m0\033[m e \033[1;36m10\033[m.
\033[1mSerá que você consegue adivinhar qual foi?\033[m''')
acertou = False
tentativas = 0
while not acertou:
    palpite = int(input('\033[1;33mDigite seu palpite:\033[m '))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > 10:
            print('\033[1mValor inválido! Tente novamente!\033[m')
        elif palpite < computador:
            print('\033[1mO número que eu pensei é MAIOR que \033[1;36m{}\033[m. \033[1mTente novamente!\033[m'.format(palpite))
        elif palpite > computador:
            print('\033[1mO número que eu pensei é MENOR que \033[1;36m{}\033[m. \033[1mTente novamente!\033[m'.format(palpite))
print('\033[1mVocê acertou na {}ª tentativa! Parabéns!\033[m'.format(tentativas))
