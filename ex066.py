'''Crie um programa que leia varios numeros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando a flag).'''

cont = 0
soma = 0
while True:
    numero = int(input('Digite um número inteiro [999 para parar]: '))
    if numero == 999:
        break
    cont = cont + 1
    soma = soma + numero
print(f'Ao todo foram digitados {cont} números e a soma total foi {soma}')