# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# calculo da porcentagem -> valor * qual porcentagem calcular / 100

salario = float(input('Qual é o salário do funcionário: R$'))
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, salario+(salario*15/100)))
