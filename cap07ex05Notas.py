
with open('notas.txt', 'a+') as arq:
    leitura = arq.read()
    print(leitura)
    arq.write('Observação a ser adicionada ao notas.txt')




pass