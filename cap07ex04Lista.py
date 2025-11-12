lista = []

print('Digite os itens da sua lista de compras.')
print('Quando terminar, digite "fim".')

while True:
    item = input('Item: ').strip()
    if item.lower() == 'fim':
        break
    lista.append(item)

with open('lista_de_compras.txt', 'w+') as arq:
    for item in lista:
        arq.write(item + "\n") 

print(f'Lista salva no arquivo com sucesso!')

pass