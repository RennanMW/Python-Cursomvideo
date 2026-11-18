# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] <= 5:
    aluno['situacao'] = 'Reprovado'
elif aluno['media'] > 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'

print('-=' * 30)
for key, value in aluno.items():
    print(f'O {key} é igual a {value}')
