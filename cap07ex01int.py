
while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Erro. Por favor, digite um número inteiro válido.')
        
