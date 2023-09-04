print('\033[1;31mMédia escolar\033[m')
print('\033[1;34m-=-\033[m' * 25)
nome = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a nota do teste: '))
n2 = float(input('Digite a nota da prova: '))
media = (n1 + n2) / 2
print('Como nota {:.1f} no teste e {:.1f} na prova, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 6:
    print('O aluno {} está \033[1:34mAPROVADO\033[m!'.format(nome))
elif media >= 5 and media < 6:
    print('O aluno {} está de \033[1:33mRECUPERAÇÃO\033[m!'.format(nome))
else:
    print('O aluno {} está \033[1:31mREPROVADO\033[m!'.format(nome))
