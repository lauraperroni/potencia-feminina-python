
# Funções

def soma(num1, num2): # definição da função soma
    calculo = num1+num2
    print(f'O resultado da soma é: {calculo}')

def subtracao(num1, num2): # definição da função soma
    calculo = num1-num2
    print(f'O resultado da subtração é: {calculo}')
    multiplicacao(num1, num2) # chamada de função dentro de função

def multiplicacao(num1, num2): # definição da função soma
    calculo = num1*num2
    print(f'O resultado da multiplicação é: {calculo}')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2)
subtracao(num1, num2)
