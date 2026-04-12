'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o emprestimo será negado.'''

valorImovel = int(input('Qual é o valor do imovel: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento?: '))

# Calcula o prazo que será pago o financiamento em meses, dividindo os anos em meses.
prazo = financiamento * 12

# Calcula a parcela que será paga com base no valor total do imovel dividido pelos meses a ser pago.
parcela = valorImovel / prazo

if parcela > (salario * 30 /100): # Calcula o valor da prestação em relação ao salario, nao pode ser maior que 30%.
    print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valorImovel, financiamento, parcela))
    print('O emprestimo pode ser negado!')
else:
    print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valorImovel, financiamento, parcela))
    print('O emprestimo pode ser concedido!')