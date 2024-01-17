def divisao(a,b):
        try:
            result = a/b
            print(result)
        except ZeroDivisionError:
              print('Impossível dividir um valor por zero.')
        except TypeError as e:
              print(f'Erro: o tipo do dado informado não está correto. \n Detalhes: {e}')

    
#divisao(10,2)
#divisao(10,0)
divisao(10, 'Womakerscode')
