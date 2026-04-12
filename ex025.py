# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é o seu nome completo? ')).strip().title()
silva = 'Silva' in nome
print('Seu nome tem silva? {}'.format(silva))