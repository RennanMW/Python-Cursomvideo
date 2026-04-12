# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for cont in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(cont)))
    if cont == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('O maior peso digitado foi {}Kg'.format(maiorPeso))
print('O menor peso digitado foi {}Kg'.format(menorPeso))