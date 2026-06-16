'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

from random import randint

numeros = tuple(randint(0, 9) for c in range(0, 5))
print(numeros)

maiorNumero = max(numeros)
print(f'O maior valor sorteado foi: ', maiorNumero)

menorNumero = min(numeros)
print(f'O menor valor sorteado foi: ', menorNumero)