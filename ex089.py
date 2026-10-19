'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = list()
aluno = []
# Cadastro dos alunos em listas
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()

    # Verificação da continuação de preenchimento das lista de alunos.
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-=' * 30)
print(f'{"N°":<4}{"NOME":^10}{"MÉDIA":>8}')
print('-' * 30)

# O for percorre o comprimento da lista alunos e monta a tabela com indice, nome e média.
for numero, aluno in enumerate(alunos):
    print(f'{numero:<4}{aluno[0]:^10}{aluno[3]:>8.1f}')
print('-' * 30)

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break

    # Verifica o comprimento da lista, se o numero digitado for maior que o indice, retorna a mensagem.
    elif opcao >= len(alunos):
        print('Aluno não encontrado!')

    # Mostra as informações do aluno de acordo com o indice selecionado na opção.
    else:
        print(f'Notas do {alunos[opcao][0]} são: '
              f'{alunos[opcao][1]} e {alunos[opcao][2]}')
