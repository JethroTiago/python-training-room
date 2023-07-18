print('Distâncias')
print('')
m = float(input('Qual é a distância em metros? '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m/ 100
km = m / 1000
print('A distancia {}m digitada, equivale a:'.format(m))
print('{}km (Quilômetro)'.format(km))
print('{}hm (Hectômetro)'.format(hm))
print('{}dam (Decâmetro)'.format(dam))
print('{:.0f}dm (Decímetro)'.format(dm))
print('{:.0f}cm (Centímetro)'.format(cm))
print('{:.0f}mm (Milímetro)'.format(mm))
# Unidades internacionais de medidas: Quilômetro (km), Hectômetro (hm), Decâmetro (dam),
# metro (m), Decímetro (dm), Centímetro (cm) e Milímetro (mm).