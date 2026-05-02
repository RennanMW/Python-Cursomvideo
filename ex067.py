'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o valor for 0'''

while True:
    valor = int(input('Quer ver a tabuada de qual número?: '))
    if valor == 0:
        break
    print('-' * 35)
    for contador in range(1, 11):
        print(f'{valor} X {contador:2} = {valor * contador}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
