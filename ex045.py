# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep
# Criação dos itens do jogo em lista e de forma randomica
lista = ('PEDRA', 'PAPEL', 'TESOURA')
computador = choice(lista)

# Seleção das opções do jogador
jogador = int(input('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 15)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(lista[jogador]))
print('-=' * 15)

# Testes logicos dos itens do jogo
if lista[jogador] == 'PEDRA' and computador == 'PAPEL':
    print('COMPUTADOR VENCE')
elif lista[jogador] == 'PEDRA' and computador == 'TESOURA':
    print('JOGADOR VENCE')
elif lista[jogador] == 'PAPEL' and computador == 'PEDRA':
    print('JOGADOR VENCE')
elif lista[jogador] == 'PAPEL' and computador == 'TESOURA':
    print('COMPUTADOR VENCE')
elif lista[jogador] == 'TESOURA' and computador == 'PEDRA':
    print('COMPUTADOR VENCE')
elif lista[jogador] == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCE')
else:
    print('EMPATE')
