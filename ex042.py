'''Refaça o desafio 35 dos triangulos, adicionando o recurso de mostrar que tipo de triangulo será formado.
EQUILATERO: todos os lados iguais.
ISÓSCELES: dois lados iguais e um diferente.
ESCALENO: todos os lados diferentes.'''

ladoA = float(input('Digite o comprimento da primeira reta: '))
ladoB = float(input('Digite o comprimento da segunda reta: '))
ladoC = float(input('Digite o comprimento da terceira reta: '))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print('Com os segmentos de reta informados, pode se formar um triangulo!')
    if ladoA == ladoB and ladoB == ladoC:
        print('Esse triangulo que foi formado se chama EQUILATERO!')
    elif ladoA == ladoB and ladoA != ladoC or ladoB == ladoC and ladoB != ladoA or ladoC == ladoA and ladoC != ladoB:
        print('Esse triangulo que foi formado se chama ISOSCELES!')
    else:
        print('Esse triangulo que foi formado se chama ESCALENO!')
else:
    print('Com os segmentos de reta informados, não se pode formar um triangulo!')