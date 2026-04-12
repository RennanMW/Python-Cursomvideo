# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um numero para ver se ele é um numero primo: '))
dividido = 0

for c in range(1, numero + 1):
    print(c, end=' ')

for c in range(1, numero + 1):
    if numero % c == 0:
        dividido = dividido + 1

print('\nO numero {} foi divido {} vezes!'.format(numero, dividido))

if dividido == 2:
    print('por isso ele é um numero primo!')
else:
    print('por isso ele não é um numero primo!')