# Aula 6 - Tipos primitivos

`int` - numeros inteiros: 7, -4, 0, 9875
`float` - numeros reais ou ponto flutuante: 4.5, 0.076, -15.223, 7.0
`bool` - valores lógicos ou booleanos: True, False
`str` - caracteres ou strings: 'Olá', '7.5'

# Aula 7 - Operações aritméticas

+: adição
-: subtração
*: multiplicação
/: divisão
**: potência
//: divisão inteira
%: resto da divisão

Ordem de precedencia
1°: ()
2°: **
3°: *, /, //, %
4°: +, -

# Aula 8 - Utilizando módulos

Comando - `import` nome da biblioteca
Comando - `from` nome da biblioteca `import` funcionalidade

# Aula 9 Manipulando textos

Cada cadeia de caracteres são divididas em índices sempre começando em 0.

`frase = 'Curso em Vídeo Python'`

Cada string é separada por microespaçoes com indices.

Fatiamento: Possibilidade de pegar pedaços da string.
Ex:
`frase[9]`: Pega a letra referente a esse índice, "V".

`frase[9:13]`: Fatiamento que pega uma mini cadeia de caracteres dentro da cadeia inteira, nesse exemplo do número 9 até o 13 excluindo o 13, "Víde".

`frase[9:20:2]`: Fatiamento que pega uma mini cadeia de caracteres dentro da cadeia inteira, mas pulando a quantidade de letras de acordo com o ultimo número que no caso foi o 2, resultando em "VdoPto".

`frase[:5]`: Significa que não foi indicado o inicio do fatiamento, portanto começa do inicio 0, e vai até 5, excluindo o 5, "Curso"

`frase[15:]`: Mesma linha de raciocinio do exemplo anterior só que dessa vez colocando um inicio e fatiando até o final da string, "Python"

`frase[9::3]`: Significa que o fatiamento vai começar em 9 vai até o final pulando de 3 em 3 caracteres, "VePh".

Análise: Possibilidade de pegar informações sobre a cadeia de caracteres.

`len(frase)`: len vem de Lenght que significa comprimento == 21

`frase.count('o')`: Pode se contar quantas letras existem na cadeia de caracteres, nesse caso o resultado == 3

`frase.find('deo')`: Com o find o resultado da procura vai ser ond foi o primeiro encontro do valor necessitado, nesse caso == 11
Caso a string digitada no find não exista, o python retornará -1.

`'Curso' in frase`: Com o operador "in" é possivel fazer analises de strings, ele vai retornar True caso for verdadeiro e False caso não, nesse == True.

Transformação: Possibilidade de modificar strings.

`frase.upper()`: Transforma a string em maiusculas todas as letras == 'CURSO EM VÍDEO PYTHON'.

`frase.lower()`: Semelhante ao upper, ele transforma a cadeia de strings em minusculas == 'curso em vídeo python'.

`frase.capitalize()`: Faz com que somente a primeira letra da cadeia de caracteres seja maiusculo e todo resto minusculo == 'Curso em vídeo python'.

`frase.title()`: Parecido com o capitalize, o title coloca todas as primeiras letras das palavras da cadeia em maiusculo == Curso Em Video Python'.

`frase.strip()`: Função que remove espaços nas extremidades da cadeia de caracteres, tem tambem a função .rstrip e .lstrip caso queira remover apenas os espaços da direita ou da esquerda.

Divisão: dividir a cadeia de caracteres.

`frase.split()`: Divide a string em uma lista pelos espaços e cada palavra da string recebe um no indice começando em 0.

Junção: juntar strings separadas.

`'-'.join(frase)`: Junta a frase pela "condição" dentro do apostrofo que nesse caso foi o hifen.

# Aula 10 Condição (parte 1)

Condição simples e composta

Simples: `if (condição verdadeira):`
                bloco de comando

Composta: `if (condição verdadeira):`
                bloco de comando
           `else:`
                bloco de comando
