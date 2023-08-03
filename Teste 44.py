print('\033[1;34mGerenciador de pagamentos\033[m')
print('\033[1:36m{:=^44}\033[m'.format(' LOJAS PYTHON '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ \033[1:34m1\033[m ] à vista dinheiro
[ \033[1:34m2\033[m ] à vista cartão
[ \033[1:34m3\033[m ] 2x no cartão
[ \033[1:34m4\033[m ] 3x ou mais no cartão''')
forma = int(input('Digite o valor referente a opção: '))
if forma == 1:
    total = preco - (preco * 10) / 100
    print('A compra de R${} vai custar R${} no final (10% de desconto).'.format(preco, total))
elif forma == 2:
    total = preco - (preco * 5) / 100
    print('A compra de R${} vai custar R${} no final (5% de desconto).'.format(preco, total))
elif forma == 3:
    parcela = preco / 2
    print('A compra será parcelada em 2x de {} e não receberá descontos.'.format(parcela))
elif forma == 4:
    total = preco + (preco * 20) / 100
    quantidadeparcelas = int(input('Quantas parcelas? '))
    parcela = total / quantidadeparcelas
    print('Sua compra será parcelada em {}x de R${} (20% de Juros).'.format(quantidadeparcelas, parcela))
else:
    print('O valor digitado não é válido. Tente novamente.')
print('\033[1:36m{:=^44}\033[m'.format(' LOJAS PYTHON '))
print('FIM')
