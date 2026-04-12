# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 30)
print('10 primeiros termos de uma PA')
print('=' * 30)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for cont in range(primeiroTermo, primeiroTermo + (11 - 1) * razao, razao):
    print(cont , end=' -> ')
print('Acabou')