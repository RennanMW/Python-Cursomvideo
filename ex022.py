# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()
maiuscula = nome.upper()
minuscula = nome.lower()
comprimento = len(nome) - nome.count(' ')
primeiroNome = nome.split()

print('Seu nome em MAIUSCULO é: {}.'.format(maiuscula))
print('Seu nome em MINUSCULO é: {}.'.format(minuscula))
print('Seu nome tem: {} letras.'.format(comprimento))
print('Seu primeiro nome tem: {} letras.'.format(len(primeiroNome[0])))