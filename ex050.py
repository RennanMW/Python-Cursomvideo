# Desenvolva um programa que leia seis números inteiros e
#  mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for cont in range(1, 7):
    numero = int(input('Digite o {}° numero: '.format(cont)))
    if numero % 2 == 0:
        soma = soma + numero
print('A soma dos valores pares é {}'.format(soma))