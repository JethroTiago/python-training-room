print('Aprovando empréstimo')
print('\033[1;31m-=-\033[m' * 25)
valor = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
porcento = (salario * 30) / 100
parcela = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}!'.format(valor, anos, parcela))
if parcela > porcento:
    print('\033[1;31mEmprestimo negado!\031[m')
else:
    print('\033[1;32mEmpréstimo pode ser liberado!\033[m')
print('\033[1;31m=-=\033[m' * 27)
print('FIM')