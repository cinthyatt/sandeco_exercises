import numpy as np
from random import randint

lista = []
for i in range(10):
    n = randint(1, 100)
    lista.append(n)
print(lista)

vetor = np.array([lista])

media = np.mean(vetor)
variancia = np.var(vetor)
dp = np.std(vetor)

print(f'Media: {media}',
      f'\nVariancia: {variancia}',
      f'\nDesvio Padrão: {dp}'
      )