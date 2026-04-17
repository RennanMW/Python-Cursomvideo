'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F".
Caso esteja errado, peça a digitação novamente até ter uma valor correto.'''


sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))