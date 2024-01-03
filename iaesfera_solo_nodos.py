import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generar una esfera utilizando ecuaciones paramétricas
u = np.linspace(0, 2 * np.pi, 21)
v = np.linspace(0, np.pi, 31)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Crear una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Encontrar los nodos
nodos = np.array([x.flatten(), y.flatten(), z.flatten()]).T

# Dibujar los nodos
ax.scatter(nodos[:, 0], nodos[:, 1], nodos[:, 2], color='red')

# Establecer los límites del eje
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])

# Añadir etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la trama
plt.show()