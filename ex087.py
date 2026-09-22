'''Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[], [], []]
soma_par = 0
soma_terceira_coluna = 0
maior_numero = 0

# Loop que faz a leitura das posições da matriz, linha e coluna.
for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        matriz[linha].append(numero)

        if numero % 2 == 0: # Verifica se o valor digitado é par.
            soma_par = soma_par + numero

# Loop que pega o 3° valor de cada linha, ou seja, a 3° coluna da matriz e soma seus números.
for linha in range(0, 3):
    soma_terceira_coluna = soma_terceira_coluna + matriz[linha][2]

# Loop que testa se cada valor dentro da segunda linha é maior que o anterior dentro da mesma linha.
for linha in range(0, 3):
    if matriz[1]:
        if matriz[1][0] > maior_numero:
            maior_numero = matriz[1][0]
        elif matriz[1][1] > maior_numero:
            maior_numero = matriz[1][1]
        else:
            maior_numero = matriz[1][2]

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_numero}.')
