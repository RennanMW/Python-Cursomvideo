# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um numero para ve se ele é PAR ou IMPAR: '))

if numero % 2 == 0: # Verifica a divisão do numero e se o resto da divisão é 0
    print('O numero {} é PAR!'.format(numero))
else:
    print('O numero {} é IMPAR!'.format(numero))