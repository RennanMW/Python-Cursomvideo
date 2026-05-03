'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 1 1 2 3 5 8'''

print('-=' * 20)
print('Sequancia de Fibonacci')
print('-=' * 20)
#inicialização do primeiro termo, segundo termo e terceiro termo
primeirotermo = 0
segundotermo = 1
terceirotermo = primeirotermo + segundotermo

# Quantidade de termos a ser escolhidos pra ser mostrado
quantidade = int(input('Quantos termos você quer mostrar?: '))

# Mostra o primeiro e o segundo termo lado a lado
print('{} -> '.format(primeirotermo), end='')
print('{} -> '.format(segundotermo), end='')

# inicia o contador a partir do segundo termo e somando os dois primeiros 
contador = 2
soma = terceirotermo
while contador < quantidade: # enquanto a quantidade de termos for menor que a quantidade escolhida...
    print('{} -> '.format(soma), end='')

    ''' Bloco de comando que faz com que o primeiro termo termo receba o segundo, o segundo receba a soma e
    o terceiro some os novos valores'''
    primeirotermo = segundotermo
    segundotermo = terceirotermo
    terceirotermo = primeirotermo + segundotermo
    soma = terceirotermo
    contador = contador + 1
print('FIM')