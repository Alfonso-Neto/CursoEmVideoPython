from math import hypot
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))

hipo = hypot(cato, cata)

print('A hipotenusa é: {:.2f} '.format(hipo))