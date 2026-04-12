'''Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

base = int(input('Digite um numero inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BÍNARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(base)
    print('{} convertido para BINÁRIO é igual a {}'.format(base, binario[2:]))
elif escolha == 2:
    octal = oct(base)
    print('{} convertido para OCTAL é igual a {}'.format(base, octal[2:]))
elif escolha == 3:
    hexa = hex(base)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(base, hexa[2:]))
else:
    print('Opção escolhida invalida!')