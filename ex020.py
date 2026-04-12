'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')

# coloca as variaveis em uma lista
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

# variavel que recebera a lista randomizada
sequencia = shuffle(lista)
print('As sequencia de apresentação será ')
print(lista)