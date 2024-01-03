import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Dibujar los nodos de ambas esferas
ax.scatter(nodos[:, 0], nodos[:, 1], nodos[:, 2], color='red')
ax.scatter(nodos2[:, 0], nodos2[:, 1], nodos2[:, 2], color='blue')

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