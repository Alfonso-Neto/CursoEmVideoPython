from math import sin, cos, tan, radians

ang = float(input('Digite o ângulo: '))

res1 = sin((radians(ang)))
res2 = cos((radians(ang)))
res3 = tan((radians(ang)))

print('O seno de {}° é: {:.2f} \nO coseno de {}° é: {:.2f} \nA tangente de {}° é: {:.2f} '.format(ang, res1, ang, res2, ang, res3))