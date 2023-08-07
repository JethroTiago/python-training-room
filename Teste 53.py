print('\033[1;34m-=-\033[m' * 15)
print('\033[1;35mDETECTOR DE PALÍNDROMOS\033[m')
print('\033[1;34m-=-\033[m' * 15)
print('\033[1;31mOBS: Não use acentos, pontuação ou caracteres especiais!\033[m')
print('\033[1;34m-=-\033[m' * 15)
frase = str(input('\033[1mDigite uma palavra/frase:\033[m ')).strip().upper() #retirado espaços e colocado em maiúsculas
palavras = frase.split() #separa cada palavra digitada
junto = ''.join(palavras) #une as palavras digitadas
inverso = junto[::-1] #inverte as letras do fim para o início
'''for letras in range(len(junto) - 1, -1, -1): #inverte as letras do fim para o início
    inverso += junto[letras]'''
print('O inverso da palavra/frase \033[1;36m{}\033[m é \033[1;36m{}\033[m.'.format(junto, inverso))
if inverso == junto:
    print('Temos um \033[1;32mPALÍNDROMO\033[m!')
else:
    print('Essa palavra/frase \033[1;31mnão\033[m é um \033[1;32mPALÍNDROMO\033[m!')
print('\033[1;34m-=-\033[m' * 15)
print('FIM')

'''PALÍNDROMO é uma frase ou palavra que se pode ler, indiferentemente, 
da esquerda para direita ou vice-versa”. Exemplos: Osso, Ana, Radar, Renner, Roma é amor, 
Orava o Avaro, socorram-me subi no ônibus em Marrocos...'''
