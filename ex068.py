'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo'''

from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
soma = 0
vitorias = 0
derrota = 0

while True:
    computador = randint(0, 10)
    print(computador)
    valor = int(input('Diga um número: '))
    jogada = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    soma = valor + computador
    if soma % 2 == 0 and jogada == 'P':
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR')
        print('Você VENCEU! \nVamos jogar novamente...')
        vitorias = vitorias + 1
        print('-=' * 15)
    elif soma % 2 == 1 and jogada == 'I':
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('Você VENCEU! \nVamos jogar novamente...')
        vitorias = vitorias + 1
        print('-=' * 15)
    else:
        derrota = 1
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma}')
        print('Você PERDEU!')
        print('-=' * 15)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')