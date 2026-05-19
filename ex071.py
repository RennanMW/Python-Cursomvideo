'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Digite o valor do saque: '))

quantidade50 = 0
quantidade20 = 0
quantidade10 = 0
quantidade1 = 0

# Notas de 50
while True:
    if valor >= 50:
        valor -= 50
        quantidade50 += 1
    else:
        break

# Notas de 20
while True:
    if valor >= 20:
        valor -= 20
        quantidade20 += 1
    else:
        break

# Notas de 10
while True:
    if valor >= 10:
        valor -= 10
        quantidade10 += 1
    else:
        break

# Notas de 1
while True:
    if valor >= 1:
        valor -= 1
        quantidade1 += 1
    else:
        break

print(f'Notas de 50: {quantidade50}')
print(f'Notas de 20: {quantidade20}')
print(f'Notas de 10: {quantidade10}')
print(f'Notas de 1: {quantidade1}')