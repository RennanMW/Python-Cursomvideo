'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
 peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=' * 30)

jogador = int(input('Em que número pensei?: '))
computador = randint(0, 5) # Faz o programa randomizar um numero entre 0 e 5.
if jogador == computador: # Testa o numero digitado pelo usuario e verifica se é igual ao numero randomizado
    print('Processando...')
    tempo = sleep(3)
    print('PARABÉNS! Voce conseguiu me vencer!')
else:
    print('Processando...')
    tempo = sleep(3) # Faz o programa parar pela quantidade definida do argumento (3) segundos
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))