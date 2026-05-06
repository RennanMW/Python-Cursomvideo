'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

acimaMil = 0

print('-=' * 20)
print('{:^40}'.format('LOJA VENDE TUDO'))
print('-=' * 20)

nomeProduto = str(input('Nome do produto: ')).strip().title()
preco = float(input('Preço do produto: R$'))

menorPreco = preco
totalCompra = preco
produtoBarato = nomeProduto

if preco > 1000:
    acimaMil = acimaMil + 1
resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

if resposta == 'S':
    while True:
        print('-=' * 30)
        nomeProduto = str(input('Nome do produto: ')).strip().title()
        preco = float(input('Preço do produto: R$'))
        totalCompra = totalCompra + preco

        if preco < menorPreco:
            menorPreco = preco
            produtoBarato = nomeProduto

        if preco > 1000:
            acimaMil = acimaMil + 1

        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        while resposta not in 'SN':
            resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta == 'N':
            break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra foi de R${totalCompra:.2f}')
print(f'Total de produtos acima de R$1000: {acimaMil}')
print(f'O produto mais barato foi: {produtoBarato}, custando R${menorPreco:.2f}')