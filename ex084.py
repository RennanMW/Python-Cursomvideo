'''Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

# Declaração das listas e algumas variaveis 
grupo = list()
pessoa = []
cadastro = 0
maiorPeso = 0

while True:
    # Informaçõoes da lista interna que será adicionada a lista lista principal
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    maiorPeso = pessoa[1]
    menorPeso = pessoa[1]
    
    #adição da lista secundaria na lista principal
    grupo.append(pessoa[:]) # Usando o método de cópia de valores [:]
    pessoa.clear() # Limpando as informações da lista secundaria para o próximo laço 
    cadastro = cadastro + 1

    # Laço individual que percorre a lista principal e verifica se a cada indice de lista secundaria adicionada, a "pessoa" adicionada, é mais pesada que a anterior
    for p in grupo:
        if p[1] > maiorPeso:
            maiorPeso = p[1]

    # Outro laço individual que percorre a lista principal, mas que testa o menor peso
    for p in grupo:
         if p[1] < menorPeso:
              menorPeso = p[1]

    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]' )).strip().upper()[0]
    if opcao == 'N':
            break

print('-=' * 30)
print(f'Ao todo, voce cadastrou {cadastro} pessoas.')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end=' ')
for p in grupo:
      if p[1] == maiorPeso:
            print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menorPeso}Kg. Peso de ', end=' ')
for p in grupo:
     if p[1] == menorPeso:
          print(f'[{p[0]}]', end=' ')
