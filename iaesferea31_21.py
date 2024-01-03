import numpy as np
import matplotlib.pyplot as plt

# Generar una esfera utilizando ecuaciones paramétricas
u = np.linspace(0, 2 * np.pi, 21)
v = np.linspace(0, np.pi, 31)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Encontrar los nodos
nodos = np.array([x.flatten(), y.flatten(), z.flatten()]).T

# Dibujar los nodos
plt.scatter(nodos[:, 0], nodos[:, 1], color='red')

# Establecer los límites del eje y la relación de aspecto
plt.axis('square')
plt.xlim([-1.1, 1.1])
plt.ylim([-1.1, 1.1])

# Añadir etiquetas a los ejes
plt.xlabel('X')
plt.ylabel('Y')

# Mostrar la trama
plt.show()