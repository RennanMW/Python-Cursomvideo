'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de Zero até Vinte. Seu programa deverá ler um numero pelo teclado( entre 0 e 20) e mostra-lo por extenso'''

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
if numero < 0 or numero > 20: # verifica se o numero esta entre 0 e 20

    # caso não, entra em loop pedindo o numero novamente
    while True:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if numero >= 0 and numero < 21: # nova verificação e caso verdade, sai do loop
            break

if numero <= len(extenso) - 1: # Se o numero digitado for menor ou igual ao comprimento da tupla -1
    print(f'Você digitou o número {extenso[numero]}') # Mostre na tupla a posição equivalente ao numero digitado