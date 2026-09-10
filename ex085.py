'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

principal = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite {c}° valor: '))

    if numero % 2 == 0:
        principal[0].append(numero)
        principal[0].sort()
    else:
        principal[1].append(numero)
        principal[1].sort()

print('-=' * 30)
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores impares digitados foram: {principal[1]}')
