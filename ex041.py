'''A Confederação Nacional de Natação precisa de um programa que leia um ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade;
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima dos 25 anos: MASTER '''
from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - nasc
print('A idade do atleta é de {} anos.'.format(idade))

if idade <= 9:
    print('O atleta entra na categoria: MIRIM!')
elif idade > 9 and idade <= 14:
    print('O atleta entra na categoria: INFANTIL!')
elif idade > 14 and idade <= 19:
    print('O atleta entra na categoria: JUNIOR!')
elif idade > 19 and idade <= 25:
    print('O atleta entra na categoria: SÊNIOR!')
else:
    print('O atleta entra na categoria: MASTER!')