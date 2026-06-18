'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais'''

palavras = (
    'aprender',
    'python',
    'curso',
    'programar',
    'computador'
)

for palavra in palavras:
    print(f'\nNa palavra {palavra} as vogais são: ', end='')
    for letra in range(0, len(palavra)):
        if palavra[letra] in 'aeiou':
            print(palavra[letra], end=' ')