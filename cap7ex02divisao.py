while True: 
    try:
        numerador = float(input('Digite o numerador: '))
        break
    except ValueError:
        print('Erro. Digite um número válido')

while True:
    try: 
        denominador = float(input('Digite o denominador: '))
        if denominador == 0:
            raise ZeroDivisionError    
        break
    except ValueError:
        print('Erro. Digite um número válido.')
    except ZeroDivisionError:
        print('Erro. Não é possível fazer divisão por zero.')

divisao = numerador / denominador
print(f'{divisao:.2f}')


