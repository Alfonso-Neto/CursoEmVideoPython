altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

a = altura * largura
qt = a / 2

print('A sua parede de {} x {} tem a área de = {}m², a quantidade de tinta para pintar a área em questão é de: {:.3f}L de tinta'.format(altura, largura, a, qt))