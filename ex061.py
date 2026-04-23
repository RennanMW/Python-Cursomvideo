'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: ')) # primeiro termo da PA
razao = int(input('Razão: ')) # razão da PA, pula de quantos em quantos

# o contador inicia no termo indicado
contador = termo
# calculo matematico para saber o enezimo termo da PA, no caso o decimo termo
decimo = termo + (11 - 1) * razao
while contador < decimo:
    print(contador, end=' -> ')
    # faz com que o contador receba ele mesmo somando a razao informada
    contador = contador + razao
print('FIM')