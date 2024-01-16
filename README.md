# Python - Potência Feminina
Este á um repositório do curso Womakerscode e Potencia feminina sobre Python. Neste arquivo estarei fazendo anotações das aulas, sinta-se à vontade para comentar/editar :)

## Anotações do curso:

**Comentários**

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

### Função str.format()

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



