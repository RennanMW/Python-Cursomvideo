'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

a vista dinheiro/cheque: 10% de desconto

a vista no cartão: 5% de desconto

Em até 2x no cartão: preço normal

3x ou mais no cartão: 20x de juros'''

precoProduto = float(input('Qual é o preço do produto: R$'))

print('''Opções de pagamento:
1 - A vista dinheiro / cheque
2 - A vista no cartão (crédito ou débito)
3 - 2x no cartão
4 - 3x ou mais no cartão''')
opcao = int(input('Qual a opção escolhida?: '))

if opcao == 1:
    desconto = precoProduto - (precoProduto * 10 / 100)
    print('Com o pagamento a vista no dinheiro ou cheque, voce acaba de ganhar um desconto de 10% no seu produto!')
    print('Ele que estava custando R${:.2f}, passa a custar R${:.2f}'.format(precoProduto, desconto))

elif opcao == 2:
    desconto = precoProduto - (precoProduto * 5 / 100)
    print('Com pagamento a vista no cartão, voce acaba de ganhar um desconto de 5% no seu produto!')
    print('Ele estava custando R${:.2f}, passa a custar R${:.2f}'.format(precoProduto, desconto))

elif opcao == 3:
    print('A sua compra foi no valor de R${:.2f}, cada parcela será de R${:.2f}'.format(precoProduto, precoProduto / 2))

else:
    parcelamento = int(input('Quantas vezes será parcelado: '))
    juros = precoProduto * (20 / 100)
    print('A sua compra foi de R${:.2f} em {}x.'.format(precoProduto, parcelamento))
    print('As parcelas da sua compra serão de R${:.2f}.'.format((precoProduto + juros) / parcelamento))
    print('O valor total a ser pago no final será de R${:.2f}'.format(precoProduto + juros))