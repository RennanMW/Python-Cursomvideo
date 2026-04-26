'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

flag = 0
numero = 0
soma = 0
contador = 0
while flag != 999:
    numero = int(input('Digite um número: '.format(numero)))
    contador = contador + 1
    flag = numero
    soma = soma + numero
print('Foram {} números digitados e a soma total dos numeros é {}'.format(contador - 1, soma - flag))