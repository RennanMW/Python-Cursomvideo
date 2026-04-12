# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

# regra matematica de triangulos, desigualdade triangular, que testa se segmentos de retas podem formar um triangulo.
if a + b > c and a + c > b and b + c > a:
    print('Com os segmentos de reta informados, pode se formar um triangulo!')
else:
    print('Com os segmentos de reta informados, não se pode formar um triangulo!')