produto = float(input('Digite o preço do produto: '))
desc = produto - (0.05 * produto)

print('O preço de seu produto com 5% de desconto é de: {:.2f}'.format(desc))