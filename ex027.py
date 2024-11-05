nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
pri = dividido[0]
ult = dividido[-1]
print('O primeiro nome da pessoa é {} e o último {} '.format(pri,ult))