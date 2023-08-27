print('\033[1;34m=-=\033[m' * 15)
print('\033[1;33mCONTANDO VOGAIS EM TUPLA\033[m')
print('\033[1;34m=-=\033[m' * 15)
palavras = ('aprender', 'programar', 'linguagem', 'Python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as VOGAIS ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
