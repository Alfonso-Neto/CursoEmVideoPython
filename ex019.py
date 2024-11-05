import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do teceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

res = (a1, a2 ,a3 ,a4)

sort = random.choice(res)

print('O aluno sorteado foi: {}'.format(sort))