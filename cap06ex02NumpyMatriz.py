import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
matriz2 = np.array([[7, 4, 1], [8, 5, 2], [9, 6, 35]])

'''soma = np.add(matriz1, matriz2)
subt = np.subtract(matriz1, matriz2)'''

'''soma = matriz1 + matriz2
subt = matriz1 - matriz2
multiply = matriz1 * matriz2 #multiplica número a número
multiplic = np.dot(matriz1, matriz2) #multiplicação matricial

print(soma)
print(subt)
print(multiply) 
print(multiplic)'''

transposta = matriz2.T
print(transposta)

det = np.linalg.det(matriz2)
det1 = np.linalg.det(matriz1)
print(det, det1)

'''#Grafico que explica porque essa matriz tem determinante igual a zero
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vetores
v1 = np.array([7, 4, 5])
v2 = np.array([8, 5, 2])
v3 = np.array([9, 8, 3])

# Plotando
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origem
origin = [0, 0, 0]

# Desenhando vetores
ax.quiver(*origin, *v1, color='r', label='v1')
ax.quiver(*origin, *v2, color='g', label='v2')
ax.quiver(*origin, *v3, color='b', label='v3')

# Limites do gráfico
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_zlim([0, 10])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()'''