'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
Media abaixo de 5.0: reprovado
Media entre 5.0 e 6.9: recuperação
Media 7.0 ou superior: aprovado'''

primeiraNota = float(input('Digite a primeira nota do aluno: '))
segundaNota = float(input('Digite a segunda nota do aluno: '))
media = (primeiraNota + segundaNota) / 2
print('A média do aluno foi de {:.1f}'.format(media))

if media < 5.0:
    print('O aluno está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno foi APROVADO!')