'''Escreva um programa que leia dois numeros inteiros e compare-os,
se o primeiro valor é maior
se o segundo valor é maior
nao existe valor maior, os dois são iguais'''

primeiroNumero = int(input('Digite um numero inteiro: '))
segundoNumero = int(input('Digite o segundo numero: '))

if primeiroNumero > segundoNumero:
    maior = primeiroNumero
    print('O primeiro numero é maior!')
elif segundoNumero > primeiroNumero:
    maior = segundoNumero
    print('O segundo numero é maior!')
else:
    print('Os dois valores são iguais!')