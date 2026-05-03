'''Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo'''

from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
soma = 0
vitorias = 0
derrota = 0

while True:
    jogada = ' '
    computador = randint(0, 10) # Faz o computador ramdomizar um numero a cada loop
    valor = int(input('Diga um número: '))

    # Esse loop faz a verificação da jogada, enquanto o valor digitado não for P ou I, ele vai pedir novamente
    while jogada not in 'PI':
        jogada = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]

    # Soma os "Dedos" que vc e o computador jogou
    soma = valor + computador

    # Verificação se as jogadas juntas foram PAR e se vc escolheu PAR
    if soma % 2 == 0 and jogada == 'P':
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR')
        print('Você VENCEU! \nVamos jogar novamente...')
        vitorias = vitorias + 1
        print('-=' * 15)

    # Verificação se as jogadas juntas foram Ímpar e se vc escolheu Ímpar
    elif soma % 2 == 1 and jogada == 'I':
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        print('Você VENCEU! \nVamos jogar novamente...')
        vitorias = vitorias + 1
        print('-=' * 15)
    
    # Caso nenhuma das opções acima seja verdadeira o else joga pra fora do laço
    else:
        derrota = 1
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma}')
        print('Você PERDEU!')
        print('-=' * 15)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')