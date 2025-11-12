
with open('clientes.csv', 'r') as arq:
    for linha in arq:
        linha = linha.strip()
        if linha == '':
            continue
        
        print(linha)