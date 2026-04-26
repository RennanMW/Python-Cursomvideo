'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 1 1 2 3 5 8'''

print('-=' * 20)
primeirotermo = 0
segundotermo = 1
terceirotermo = primeirotermo + segundotermo
quantidade = int(input('Quantos termos você quer mostrar?: '))
print('{} -> '.format(primeirotermo), end='')
print('{} -> '.format(segundotermo), end='')
contador = 2
soma = terceirotermo
while contador < quantidade:
    print('{} -> '.format(soma), end='')
    primeirotermo = segundotermo
    segundotermo = terceirotermo
    terceirotermo = primeirotermo + segundotermo
    soma = terceirotermo
    contador = contador + 1
print('FIM')