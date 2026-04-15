'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaIdade = 0
maiorIdade = 0
homemVelho = ''
mulherJovem = 0

for pessoas in range(1, 5):
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual é o seu sexo (M/F): ')).upper()
    if pessoas == 1 and sexo == 'M':
        maiorIdade = idade
        homemVelho = nome
    else:
        if idade > maiorIdade and sexo == 'M':
            maiorIdade = idade
            homemVelho = nome
    if sexo == 'F' and idade < 20:
        mulherJovem = mulherJovem + 1
    somaIdade = somaIdade + idade
    mediaIdade = somaIdade / 4

print('Média de idade de todos os individuos é: {}'.format(mediaIdade))
print('O homem mais velho do grupo tem {} anos e se chama: {}'.format(maiorIdade, homemVelho))
print('A quantidade de mulheres menores de 20 anos é: {}'.format(mulherJovem))
