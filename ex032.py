# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para ver o ano atual: '))

if ano == 0: 
    ano = date.today().year  # Método que pega a data atual da maquina onde o programa ta rodando

# Testa a condição se ano é bissexto ou nao
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO!'.format(ano))