'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

opcao = 0
primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))
while opcao != 5:
    print('-=' * 20)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        soma = primeiroValor + segundoValor
        print('A soma entre {} e {} é {}'.format(primeiroValor, segundoValor, soma))
    elif opcao == 2:
        multiplicação = primeiroValor * segundoValor
        print('O resultado de {} x {} é {}'.format(primeiroValor, segundoValor, multiplicação))
    elif opcao == 3:
        if primeiroValor > segundoValor:
            maior = primeiroValor
        else:
            maior = segundoValor
        print('Entre {} e o {} o maior valor é {}'.format(primeiroValor, segundoValor, maior))
    elif opcao == 4:
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))
    else:
        print('Opção invalida! Tente novamente!')
