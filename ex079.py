'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
valor = int(input('Digite um valor: '))
valores.append(valor)
print('Valor adicionado com sucesso...')

while True:
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')

valores.sort()
print('Voce digitou os valores {}'.format(valores))