
def contar_vogais(palavra):
    vogais = []
    for letra in palavra:
        if letra in 'aeiou':
            vogais.append(letra)

    return len(vogais)

palavra = input('Digite a palavra pra que eu conte as vogais: ')
num_vogais = contar_vogais(palavra)
print(f'O número de vogais em "{palavra}" é: {num_vogais}')