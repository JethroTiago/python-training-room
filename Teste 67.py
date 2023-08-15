print('\033[1;36m-=-\033[m' * 15)
print('\033[1;35mTABUADA V3.0\033[m')
while True:
    print('\033[1;36m-=-\033[m' * 15)
    print('Digite 0 para finalizar o programa!')
    valor = int(input('\033[1mDigite um valor para verificar sua tabuada:\033[m '))
    if valor <= 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c:2} = {valor * c:2}')
print('\033[1mPROGRAMA FINALIZADO!\033[m')
