# Python - Potência Feminina
Este á um repositório do curso Womakerscode e Potencia feminina sobre Python. Neste arquivo estarei fazendo anotações das aulas, sinta-se à vontade para comentar/editar :)

## Anotações do curso:

### **Comentários**

```#``` é uma forma de comentar o código.

```'''comentário'''``` é uma forma de comentar mais de uma linha.

### **Variáveis**

São nomes que damos a valores, em python existem:

| Nome da Variável  | O que ela é                                   | Exemplo                  |
| -------------     |:---------------------------------------------:|:------------------------:|
| INT               |   Números inteiros                            |  1, 5, 20, 20000, 400    |
| FLOAT             |   Números com ponto flutuante (fracionados)   |  1.5, 5.2, 2000.43       |
| STRING            |   Textos                                      | 'Isadora' 'WoMakersCode' |
| BOOL              |   Operador lógico                             | True, False              |



**Int** se declara ```numero = int()```

**Float** se declara ```flutuante = float()```

**String** se declara ```textinho = int()```

**Bool** se declara ```logicos = bool()```


### **Operações Matemáticas**

* Soma: + ``` soma = (numero1 + numero2) ```
* Subtração: - ``` subtracao = (numero1 - numero2) ```
*  Multiplicação: * ``` multiplicacao = (numero1 * numero2) ```
* Divisão: / ``` divisao = (numero1 / numero2) ```
* Divisão inteira: //  ``` divisaoint = (numero1 // numero2) ```

**Incremento, decremento e resto de divisão**

Para incrementar um valor, utilizamos: ```valor +=1```
Para decrementar um valor, utilizamos: ```valor -=1```
Para obter o resto de uma divisão, utilizamos: ```valor1 % valor2```

**Ordem de precedência**

Python segue a matemática básica, então quando fazemos ```2+5*5``` ele retornará ```27```.
Se quisermos realizar operações em outra ordem, é exatamente como na matemática: colocamos parênteses. Nesse caso ```2+5*(5)``` retornará ```35```.


**Operadores relacionais**

* ```==``` é 'igual'
* ```>``` é 'maior que'
* ```>=``` é 'maior ou igual'
* ```<``` é 'menor'
* ```<=``` é 'menor ou igual'
* ```!=``` é 'diferente'


### Formatação de Mensagens

Para formatar textos e variáveis, colocando textos e variáveis em um mesmo print, devemos utilizar o ```f('')```, colocando o texto dentro dos ```''``` e as variáveis dentro de chaves, como ```{variável}```. Veja abaixo um caso errado de formatação, e a forma correta:

```print(A soma dos números digitados é: + soma)``` <- ERRADO

```print(f'A soma dos números digitados é: {soma})``` <- CORRETO

**Função str.format()**

Para formatarmos uma variávem em um print, pdemos utilizar a str.format(). Exemplo:

```
valor = 45.03645
print(f'{valor:.2f}') 
```
Assim o número será printado com duas casas decimais, ou seja: ```45.03```

Mais um exemplo, com string:

```
nome = 'Laura'
idade = 22
print(f'Olá {nome}, você tem {idade} anos')
```
Ou apenas:

```print('Olá {}, você tem {} anos'.format('Laura', 22))```

### Estruturas condicionais

**IF-ELSE**

Para verificar se uma informaão é verdadeira ou falsa. Só executa caso o trecho seja verdadeira. Exemplo:


```
if 1 > 2 :
    print('1 é maior que 2)
else : 
    print('1 não é maior que 2)
```

**WHILE**

Serve para fazer um código enquanto uma informação é verdadeira. 
Precisamos ter um parâmetro de parada, se não o código vai rodar para sempre. Exemplo:

```
numero = int(input('Digite um número: '))
while numero == 2 :
    print('Você digitou 2')
    numero = int(input('Digite outro número: '))

```

**FOR**

Serve para fazer um código para cada item numa sequência de itens, ele executará uma instrução. Exemplo:

```
frutas = ['Maçã', 'Banana', 'Uva']
for fruta in frutas :
    print(fruta)
```

### Listas, Tuplas e Dicionários

**Listas**

É literalmente uma lista de itens, onde o primeiro a entrar é o primeiro a sair.

Criando uma lista: ```lista = []``` 

Adicionando itens à lista: ```lista.append('Maçã')```

Printando toda a lista: ```print(lista)```

Para adicionar input do usuário:
```
fruta = input('Digite sua fruta: ')
lista_frutas.append(fruta)
```

**Tuplas**

São listas que não podem ter valores alterados. 

Criando uma tupla: ```tupla = ()```

Adicionando itens à tupla: ```tupla.append('Caju')```

Printando toda a tupla:  ```print(tupla)```

Para adicionar input do usuário: 
```
fruta = input('Digite sua fruta: ')
lista_frutas.append(fruta)
```


**Dicionários**

É um dicionário, onde se adicionam valores a significados. 

Criando um dicionário: ```dicionario = {'Chave': 'valor'}```


Adicionando itens ao dicionário: ```dicionario['maca'] = 'é uma fruta'```

Printando todo o dicionário: ```print(dicionario)```

Para adicionar input do usuário:  

```
chave = input('Digite sua chave: ')
valor = input('Digite seu valor: ')

dicionario[chave] = valor
```


### Funções em Python

* Funções são um grupo de instruções relacionadas que executa uma tafera.
* Instruções ficam dentro da função.
* Funções tem de ser chamadas, se não não funcionam.
* Podem ser chamadas dentro de outras funções
* Podem e devem ter **parâmetros**

Exemplo: 

```
def soma(num1, num2): 
    calculo = num1+num2
    print(f'O resultado da soma é: {calculo}')

soma(num1, num2)
```


### Manipulação de Arquivos 

Para manipular arquivos em Python, temos algumas propriedades:

**Open (abertura de arquivo)**

```arquivo_leitura = open(file, "r")```<-- Com o 'r', estamos apenas fazendo leitura

```arquivo_escrita = open(file, "w")```<-- Com o 'w', estamos apenas fazendo escrita

```arquivo_binário = open(file, "wb")```<-- Com o 'w', estamos apenas leitura binária

**.write (escrita em arquivo)**

```arquivo_escrita.write("Texto a ser escrito")```<-- Com o '.write', estamos escrevendo no código

**Leitura de Arquivos**

Precisa ser aberto apenas para leitura, e depois lido. Exemplo:

```
arquivo_escrita.close() <- fecha o antigo
arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
```

**Exemplo de uso**

```def multiplicacao(num1, num2): # definição da função soma
    calculo = num1*num2
    file = 'arquivo.txt'
    arquivo_leitura = open(file, "r")
    arquivo_escrita = open(file, "w")
    arquivo_binario = open(file, "wb")
    arquivo_escrita.write("Texto a ser escrito")

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

multiplicacao(num1, num2)
print(f'O resultado da multiplicação é: {calculo}')
```

**Tratamento de Exceções**

Jeito de lidar com problemas de códigos.