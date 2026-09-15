matriz = [[], [], []]

for i in range(0, 3): # Loop que controla a linha da matriz
    for j in range(0, 3): # Loop que controla as colunas da matriz
        numero = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i].append(numero) # Enquanto o loop de linha nao for alterado, será inserido um valor na coluna dessa linha.

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()