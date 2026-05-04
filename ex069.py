'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

resposta = ''
pessoasMais18 = 0
homens = 0
mulherMenos20 = 0

while True:
    print('-' * 50)
    idade = int(input('Qual é a sua idade?: '))
    sexo = str(input('Qual é o seu sexo?: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo?: [M/F]')).strip().upper()[0]
    if idade >= 18:
            pessoasMais18 = pessoasMais18 + 1
    if sexo == 'M':
         homens = homens + 1
    if idade < 20 and sexo == 'F':
        mulherMenos20 = mulherMenos20 + 1

    resposta = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('=' * 50)
print(f'Foram {pessoasMais18} pessoa(s) cadastradas tendo mais de 18 anos!')
print(f'Foram cadastradas {mulherMenos20} mulheres menos de 20 anos!')
print(f'Foram cadastrados {homens} homens!')
