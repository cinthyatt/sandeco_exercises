import csv
matriz = []

with open("notas.csv", "r", encoding="utf-8") as notas:
    leitor = csv.reader(notas)
    for linha in leitor:
        matriz.append(linha)

print(matriz)

del matriz[0]
print(matriz)

for linha in matriz:
    linha[1:] = [float(nota) for nota in linha[1:]] 
print(matriz)


'''for linha in matriz:
    soma = 0
    for nota in linha[1:]:
        soma += nota
    media = soma/(len(linha)-1)
    print(f'A média de {linha[0]} é {media:.2f}')'''

medias = []
for linha in matriz:
    nome = linha[0]
    asnotas = linha[1:]
    media = sum(asnotas) / len(asnotas)
    
    print(f'A média de {linha[0]} é {media:.2f}')
    medias.append([nome,media])

print(medias)