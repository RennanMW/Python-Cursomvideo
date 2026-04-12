'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

maior = 0
menor = 0
anoAtual = date.today().year # comando que puxa a data aual da maquina rodando o codigo

# repetição que pega o ano de nascimento das pessoas, verifica a idade e a classifica entre maior e menor
for quantidade in range(1, 8):
    nasc = int(int(input('Em que ano a {}° pessoa nasceu? '.format(quantidade))))
    idade = anoAtual - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} pessoas foram localizadas sendo maior de idade.'.format(maior))
print('E {} pessoas foram localizadas sendo menor de idade.'.format(menor))