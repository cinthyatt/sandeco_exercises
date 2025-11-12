
with open('365Historias.JPEG', 'rb') as imagem:
    with open('destino.jpg', 'wb') as destino:
        while True:
            ler = imagem.read(1024)
            if not ler:
                break
            destino.write(ler)

print('Arquivo copiado com sucesso!')

'''origem = 'imagem_original.jpg'
destino = 'imagem_copiada.jpg'

with open(origem, 'rb') as arq1:
    with open(destino, 'wb') as arq2:
        arq2.write(arq1.read())'''