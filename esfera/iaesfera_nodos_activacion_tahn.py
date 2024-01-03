import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Generar una esfera utilizando ecuaciones paramétricas
u = np.linspace(0, 2 * np.pi, 21)
v = np.linspace(0, np.pi, 31)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Generar una segunda esfera atravesada
u2 = np.linspace(0, 2 * np.pi, 21)
v2 = np.linspace(0, np.pi, 31)
x2 = np.outer(np.cos(u2), np.sin(v2))
y2 = np.outer(np.sin(u2), np.sin(v2))
z2 = np.outer(np.ones(np.size(u2)), np.cos(v2))
z2 = z2 - 1

# Crear una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Encontrar los nodos de ambas esferas
nodos = np.array([x.flatten(), y.flatten(), z.flatten()]).T
nodos2 = np.array([x2.flatten(), y2.flatten(), z2.flatten()]).T

# Crear una malla para conectar los nodos
nodos_combinados = np.concatenate((nodos, nodos2))
malla = Delaunay(nodos_combinados)

# Crear nodos de entrada y salida
nodo_entrada = nodos_combinados[0, :]
nodo_salida = nodos_combinados[-1, :]

# Dibujar los nodos y la malla
ax.scatter(nodos[:, 0], nodos[:, 1], nodos[:, 2], color='red')
ax.scatter(nodos2[:, 0], nodos2[:, 1], nodos2[:, 2], color='blue')

# Dibujar las conexiones en violeta
for simplex in malla.simplices:
    ax.plot3D([nodos_combinados[simplex[0], 0], nodos_combinados[simplex[1], 0], nodos_combinados[simplex[2], 0]],
              [nodos_combinados[simplex[0], 1], nodos_combinados[simplex[1], 1], nodos_combinados[simplex[2], 1]],
              [nodos_combinados[simplex[0], 2], nodos_combinados[simplex[1], 2], nodos_combinados[simplex[2], 2]],
              color='violet', linewidth=3)

# Dibujar el nodo de entrada y el nodo de salida
ax.scatter(nodo_entrada[0], nodo_entrada[1], nodo_entrada[2], color='green', marker='o', s=100)
ax.scatter(nodo_salida[0], nodo_salida[1], nodo_salida[2], color='yellow', marker='o', s=100)

# Añadir función de activación tanh
def tanh(x):
    return np.tanh(x)

for simplex in malla.simplices:
    ax.plot3D([tanh(nodos_combinados[simplex[0], 0]), tanh(nodos_combinados[simplex[1], 0]), tanh(nodos_combinados[simplex[2], 0])],
              [tanh(nodos_combinados[simplex[0], 1]), tanh(nodos_combinados[simplex[1], 1]), tanh(nodos_combinados[simplex[2], 1])],
              [tanh(nodos_combinados[simplex[0], 2]), tanh(nodos_combinados[simplex[1], 2]), tanh(nodos_combinados[simplex[2], 2])],
              color='violet', linewidth=3, alpha=0.5)

# Establecer los límites del eje
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-2.1, 1.1])

# Añadir etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la trama
plt.show()