# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
terceiroNumero = int(input('Digite o terceiro numero: '))

# Coloca o primeiro numero como maior e menor ao mesmo tempo 
maior = primeiroNumero
menor = primeiroNumero

# testa se o segundo numero digitado é maior que o primeiro e o terceiro
if segundoNumero > primeiroNumero and segundoNumero > terceiroNumero:
    maior = segundoNumero

# testa se o terceiro numero digitado é menor que o primeiro e o segundo
if terceiroNumero > primeiroNumero and terceiroNumero > segundoNumero:
    maior = terceiroNumero

# testa se o segundo numero digitado é menor que o primeiro e o terceiro
if segundoNumero < primeiroNumero and segundoNumero < terceiroNumero:
    menor = segundoNumero

# testa se o terceiro numero digitado é menor que o primeiro e o segundo
if terceiroNumero < primeiroNumero and terceiroNumero < segundoNumero:
    menor = terceiroNumero

print('O maior numero é o {} e o menor é o {}'.format(maior, menor))