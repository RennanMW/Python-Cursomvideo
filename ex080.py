'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort). No final, mostre a lista ordenada na tela'''

listavalor = []

for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0:
        listavalor.append(num)
    elif num > listavalor[len(listavalor) - 1]:
        listavalor.append(num)
    else:
        pos = 0
        while pos < len(listavalor):
            if num <= listavalor[pos]:
                listavalor.insert(pos, num)
                break
            pos = pos + 1

print('Os valores digitados em ordem são: {}'.format(listavalor))