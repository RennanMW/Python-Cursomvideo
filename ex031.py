'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qual é a distancia dessa viagem (Km)?: '))
print('Voce está prestes a começar uma viagem de {}'.format(distancia))

if distancia <= 200:    # Verifica se a distancia é menor que 200
    valor = distancia * 0.50 # Calcula o valor da viagem com base na distancia
    print('E o valor da sua passagem vai ser de R${:.1f}'.format(valor))
else:
    valor = distancia * 0.45
    print('E o valor da sua passagem vai ser de R${:.1f}'.format(valor))