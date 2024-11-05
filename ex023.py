n = int(input('Digite um número entre 0 e 9999: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('Nesse número existem {} unidades'.format(uni))
print('Nesse número existem: {} dezenas'.format(dez))
print('Nesse número existem: {} centenas'.format(cen))
print('Nesse número existem: {} milhares'.format(mil))
