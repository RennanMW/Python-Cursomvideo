''' Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
quantidadeTermos = 1

contador = termo # começa no termo indicado
opcao = 1 # opção tem que ser diferente da flag

# calculo pra pegar os 10 primeiros termos da PA, ja definindo 10 como o ultimo termo
enezimo = termo + (11 - 1) * razao

while opcao != 0:
    while contador < enezimo: # <- enquanto o contador for menor que o ultimo termo
        print(contador, end=' -> ')
        contador = contador + razao # soma o contador + a razao, pula de tanto em tanto
    print('PAUSA')
    quantidadeTermos = (enezimo - termo) / razao
    opcao = int(input('Quantos termos voce quer mostrar mais? (0 para finalizar) '))
    if opcao > 0:
        ''' pega a quantidade de termos a ser visto a mais == opcao, multiplica pela razao, e com esse resultado temos o novo ultimo termo da PA'''
        enezimo = enezimo + opcao * razao
        ''' aqui pegamos a quantidade a ser vista a mais == opcao, multiplicamos pela razao, e retiramos o ultimo termo ja definido antes'''
        contador = enezimo - opcao * razao
print('Progressão finalizada com {:.0f} termos mostrados.'.format(quantidadeTermos))
