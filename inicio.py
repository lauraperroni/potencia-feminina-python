
# Mensagens iniciais para o usuário
print('olá mundo')
print('olá mundo, este é meu primeiro código python')


# Tipo INTEIRO - int

numero = int(input('Digite um número: '))
print(numero)

# Tipo FLOAT - float

numero2 = float(input('Digite um número float: '))
print(numero2)

# Tipo TEXTUAL - string

frase = input('Digite uma frase: ')
print(numero)

# Tipo BOOLEANO - bolean
'''
booleano = bool(input('Digite um bolean: '))
print(booleano)
'''

# Testando todas 


print('Vou imprimir agora todas as variáveis: ')
print(numero, ' ', numero2, ' ', frase, ' ', booleano)


# Matemática

# Soma
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
soma = (numero1 + numero2)
print(soma)

# Subtração
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
subtracao = (numero1 - numero2)
print(subtracao)

# Multiplicação
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
multiplicacao = (numero1 * numero2)
print(multiplicacao)

# Divisão
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
divisao = (numero1 / numero2)
print(divisao)

# Divisão inteira
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
divisaoint = (numero1 // numero2)
print(divisaoint)

# Incremento
numero1 = int(input('Digite o número 01: '))
numero1 += 1
print(numero1)

# Decremento
numero1 = int(input('Digite o número 01: '))
numero1 -= 1
print(numero1)

# Resto de divisão
numero1 = int(input('Digite o número 01: '))
numero2 = int(input('Digite o número 02: '))
resto = (numero1 % numero2)
print(resto)

# str.format()

valor = 45.00
print(f'{valor:.2f}')


# if-else

if 1 > 2 :
    print('1 é maior que 2')
else : 
    print('1 não é maior que 2')
          

# While

numero = int(input('Digite um número: '))
while numero == 2 :
    print('Você digitou 2')
    numero = int(input('Digite outro número: '))


# FOR
    
frutas = ['Maçã', 'Banana', 'Uva']
for fruta in frutas :
    print(fruta)

# Listas 

lista_frutas = [] 
lista_frutas.append('Maçã')
lista_frutas.append('Banana')
lista_frutas.append('Uva')
print(lista_frutas)

fruta = input('Digite sua fruta: ')
lista_frutas.append(fruta)

# Tuplas 

tupla = ('maçã', 'banana', 'uva')
print(tupla)
tupla.append('Caju')
print(tupla)

fruta = input('Digite sua fruta: ')
tupla.append(fruta)

# Dicionários

dicionario = {'Chave': 'valor'}
dicionario['maca'] = 'é uma fruta'
dicionario['gato'] = 'é um animal'
dicionario['carro'] = 'é um veículo'

print(dicionario)

chave = input('Digite sua chave: ')
valor = input('Digite seu valor: ')

dicionario[chave] = valor


