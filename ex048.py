# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
# Se encontram no intervalo de 1 até 500.
soma = 0
valores_intervalo = 0
for c in range(1, 501):
    # Teste logico se o numero é multiplo de 3 e é impar
    if c % 3 == 0 and c % 2 != 0:
        # Contador: nesse caso esta sendo usado para somar quantos valores dentro do intervalo são multiplos de 3.
        valores_intervalo = valores_intervalo + 1
        # Soma dos valores que são divisiveis por 3 e o resto é 0
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(valores_intervalo, soma))
