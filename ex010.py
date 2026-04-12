reais = float(input('Qual a quantidade de dinheiro voce tem?: R$'))
dolar = 5.36
print('Com R${:.2f}, voce consegue comprar US${:.2f} dolares!'.format(reais, reais/dolar))