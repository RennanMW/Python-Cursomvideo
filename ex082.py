'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista_completa = []
lista_par = []
lista_impar = []

while True:
    lista_completa.append(int(input('Digite um número: ')))

    opcao = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
for pos, cont in enumerate(lista_completa):
    if lista_completa[pos] % 2 == 0:
        lista_par.append(lista_completa[pos])
    else:
        lista_impar.append(lista_completa[pos])

print(f'Lista completa: {lista_completa}')
print(f'Lista dos pares: {lista_par}')
print(f'Lista dos impares: {lista_impar}')