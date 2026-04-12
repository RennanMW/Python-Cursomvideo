'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se ja passou do tempo do alistamento.
Seu programa tambem deverá mostrar o tempo que falta ou que passsou do prazo'''
from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento
print('Quem nasceu em {} tem {} ano(s) em {}!'.format(nascimento, anoAtual-nascimento, anoAtual))

if idade <= 17:
    print('Faltam {} anos para seu alistamento!'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(anoAtual + (18 - idade)))

elif idade == 18:
    print('Voce deve se alistar imediatamente!')
else:
    print('Voce ja deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))