# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
numeroReal = float(input('Digite um valor (com casas decimais): '))
print('O numero digitado foi {} e sua parte inteira é {}'.format(numeroReal, trunc(numeroReal)))