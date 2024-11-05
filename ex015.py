km = float(input('Informe a quilometragem percorrida pelo carro alugado: '))
dias = float(input('Por quantos dias esse carro foi alugado? '))

prct = (60 * dias) + (0.15 * km)

print('O total a pagar pelo o aluguel do carro é de: R${}'.format(prct))