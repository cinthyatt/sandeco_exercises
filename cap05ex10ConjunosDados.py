lista1 = ['Ana', 'Jose', 'Marcos', 'Marcela', 'Clara', 'Diego', 'Gabi', 'Norberto', 'Osvaldo', 'Antonio', 'Maria', 'Teresa', 'Carla']
lista2 = ['Pedro', 'Carlos', 'Ana', 'Joaquim', 'Diego', ' Parcel', 'Rasmus', 'Maria']

conj1 = set(lista1)
conj2 = set(lista2)

ambos = conj1.intersection(conj2)
print(f'Participaram de ambos os eventos: {ambos}')
    
primeiro = conj1.difference(conj2)
print(f'Participaram só do primeiro evento: {primeiro}')

segundo = conj2.difference(conj1)
print(f'Participaram só do segundo evento: {segundo}')
