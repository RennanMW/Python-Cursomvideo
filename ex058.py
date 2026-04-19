'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(1, 10) # Faz o computador randomizar numeros de 1 até 10

print('Acabei de pensar em um número entre 1 e 10.')
print('Será que você consegue advinhar qual foi?')
palpite = int(input('Qual é o seu palpite?: '))
tentativas = 0

while palpite != computador:
    if palpite < computador:
        print('Mais... Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite?: '))
    else:
        print('Menos... Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite?: '))
    tentativas = tentativas + 1 

print('Acertou! com {} tentativas. Parabéns!'.format(tentativas))
