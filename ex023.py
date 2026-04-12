# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# pega o numero digitado pelo usuario

numero = int(input('Digite um número: '))
'''numeroString = str(numero) # transforma o numero em string
print('Analisando o numero {}'.format(numero))
print('Unidade: {}'.format(numeroString[3]))
print('Dezena: {}'.format(numeroString[2]))
print('Centena: {}'.format(numeroString[1]))
print('Milhar: {}'.format(numeroString[0]))'''


# Forma matematica de fatiamento de numero

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o numero {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))