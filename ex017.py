'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''
from math import hypot
primeiroLado = float(input('Medida do cateto oposto (cm): '))
segundoLado = float(input('Medida do cateto adjacente (cm): '))
print('As medidas informadas foram {}cm e {}cm'.format(primeiroLado, segundoLado))
print('A hipotenusa do do triangulo retangulo é {:.2f}cm'.format(hypot(primeiroLado, segundoLado)))

'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 1/2
'''