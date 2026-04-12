# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um numero para ver sua tabuada: '))
for contador in range(1, 11):
    print('{} X {:2} = {}'.format(numero, contador, contador * numero))