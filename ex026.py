frase = str(input('Digite uma frase: '))
la = frase.lower().count('a')
car = frase.lower().find('a')+1
ult = frase.rfind('a')+1
print('Nessa frase aparecem {}x, a letra "A"'.format(la))
print('Ela aparece na primeira vez na posição {} '.format(car))
print('E pela última vez na posição {} '.format(ult))