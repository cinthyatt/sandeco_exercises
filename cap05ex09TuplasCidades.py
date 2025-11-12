lista = [('Manaus', 32), ('Sao Paulo', 25), ('Rio de Janeiro', 35), ('Porto Alegre',20)]

alta = lista[0][1]
baixa = lista[0][1]
cidade_alta = None
cidade_baixa = None

for cidade in range(len(lista)):
    if lista[cidade][1] > alta:
        alta = lista[cidade][1]
        cidade_alta = lista[cidade][0]

    if lista[cidade][1] < baixa:
        baixa = lista[cidade][1]
        cidade_baixa = lista[cidade][0]

print(f'A temperatura mais alta é na cidade {cidade_alta} e a mais baixa é na cidade {cidade_baixa}.')