'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

numero = int(input('Digite um número inteiro: '))
opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
contador = 1
soma = numero
media = 0
maior = numero
menor = numero

while opcao != "N":
    numero = int(input('Digite um número inteiro: '))
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    contador = contador + 1
    soma = soma + numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
media = soma / contador
print('Você digitou {} números e a média foi {:.2f}'.format(contador, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))