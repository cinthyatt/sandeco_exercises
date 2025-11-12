
try: 
    with open('dados.txt', 'r') as arq:
        file = arq.read()

except FileNotFoundError: 
    print('Arquivo não encontrado!')

pass