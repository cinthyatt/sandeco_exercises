import numpy as np

'''array = np.array([1, 2, 3, 4, 5])
array_dobro = array *2
 
print(array_dobro)'''

#np.array converte uma lista em um array/vetor
'''vetor = np.array([1, 2, 3, 4, 5])

print(vetor)'''

'''#Soma de vetores
vetor1 = np.array([1, 2, 3])
vetor2 = np.array([4, 5, 6])

soma = vetor1 + vetor2
print(soma)'''

'''#Calculo da media dos elementos do vetor
vetor = np.array([10, 20, 30, 40, 50])
media = np.mean(vetor)
print(media)'''

'''#Indexaçao e fatiamento
vetor = np.array([10, 20, 30, 40, 50])
sub_vetor = vetor[1:4]
print(sub_vetor)'''

'''#Matriz
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
matriz_transposta = matriz.T
print(matriz_transposta)'''

'''#multiplicação de matrizes (não é elemento a elemento: [1x5+2x7, 1x6+2x8] [3x5+4x7, 3x6+4x8])
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
produto = np.dot(matriz1, matriz2)
print(produto)'''

'''#Calcular determinante
matriz = np.array([[1, 2], [3, 4]])
determinante = np.linalg.det(matriz)
print(determinante)'''

matriz = np.array([1, 2, 3, 4, 5, 6])
matriz_reshape = matriz.reshape(2, 3) #faz matriz com 2 linhas e 3 colunas
print(matriz_reshape)