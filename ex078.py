'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor para a posição {}: '.format(cont))))

for cont, valor in enumerate(valores):
    if cont == 0:
        maiorValor = valor
        menorValor = valor
    else:
        if valor > maiorValor:
            maiorValor = valor
        if valor < menorValor:
            menorValor = valor

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maiorValor} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == maiorValor:
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {menorValor} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == menorValor:
        print(f'{c}...', end='')
