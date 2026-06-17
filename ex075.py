'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares'''

numeros = ((int(input('Digite um número: '))),
           (int(input('Digite outro número: '))),
           (int(input('Digite mais um número: '))),
           (int(input('Digite o ultimo número: '))))
print(f'Voce digitou os numeros {numeros}')
if numeros[0] != 9 and numeros[1] != 9 and numeros[2] != 9 and numeros[3] != 9:
    print('O numero 9 não apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi digitado!')

print('Os numeros pares digitados foram:')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}')