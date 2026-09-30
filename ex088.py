'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from time import sleep
from random import randint

mega = []
jogo = []
print('-' * 40)
print('SORTEIO DE NÚMEROS PARA A MEGA SENA')
print('-' * 40)
jogos = int(input('Quantos jogos quer que eu sorteie?: ')) # Define a quantidade de jogos a serem sorteados

for contador in range(0, jogos):
    for cont in range(0, 6):
        numero = randint(1, 60) # Randomiza um número de 1 a 60
        if numero not in jogo:
            jogo.append(numero) # Adiciona a lista o número sorteado
        jogo.sort() # Organiza a lista de forma crescente
    mega.append(jogo[:]) # Pega uma copia da lista criada
    jogo.clear() # Limpa o conteudo da lista para receber novos valores

print('Processando...')
sleep(3)

print('-=' * 30)
for cont in range(0, jogos):
    print(f'Jogo {cont + 1}: {mega[cont]}')
    sleep(1)    
print('-=' * 30)
