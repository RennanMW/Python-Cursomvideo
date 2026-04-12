'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''

'''A variavel frase ja tem metodos imbutidos de tirar os espaços no começo e no fim == strip
joga ela em maiuscula == upper
divide ela pelos espaços em cada palavra == split'''
frase = str(input('Digite uma frase: ')).strip().upper().split()
'''a variavel juntar usa um metodo join para juntar as palavras usando de base o campo "caracter" escolhido antes do join'''
juntar = ''.join(frase)
inverso = ''

'''Este for abaixo percorre a frase da ultima posição = len(juntar) - 1, até a primeira posição menos 1, regredindo'''
for letra in range(len(juntar) -1, -1, -1):
    # essa variavel, na verredura da frase adiciona a ultima letra da frase em sua primeira gerando o inverso da frase.
    inverso = inverso + juntar[letra] 

print('O inverso de: {} é {}'.format(juntar, inverso))

if inverso == juntar:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')