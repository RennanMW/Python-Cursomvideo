'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:                                                                                                                           

A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente.

C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
contnum = 0

while True:
    numero = int(input('Digite o valor desejado: '))
    lista.append(numero)
    contnum = contnum + 1

    opcao = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'Voce digitou {contnum} elementos.')
lista.sort(reverse=True)
print('Os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não está na lista!')