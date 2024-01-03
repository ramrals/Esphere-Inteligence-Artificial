import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generar una esfera utilizando ecuaciones paramétricas
u = np.linspace(0, 2 * np.pi, 21)
v = np.linspace(0, np.pi, 8)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Crear una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar la esfera
ax.plot_surface(x, y, z)

# Establecer los límites del eje
ax.set_xlim([-1.1, 1.1])
ax.set_ylim([-1.1, 1.1])
ax.set_zlim([-1.1, 1.1])

# Añadir etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Definir los pesos de las conexiones
pesos = np.random.rand(len(nodos), len(nodos))

# Definir la función de activación
def funcion_activacion(x):
    return 1 / (1 + np.exp(-x))

# Definir la función de entrenamiento
def entrenamiento(entradas, salidas):
    # Calcular la salida de la red
    salidas_red = np.dot(entradas, pesos)
    salidas_red = funcion_activacion(salidas_red)

    # Calcular el error
    error = salidas - salidas_red

    # Actualizar los pesos
    pesos += 0.1 * np.dot(entradas.T, error)

# Cargar los datos de entrada
entradas = np.loadtxt('path/to/your/data.txt')

# Cargar los datos de salida
salidas = np.loadtxt('path/to/your/labels.txt')

# Entrenar la red
for i in range(100):
    entrenamiento(entradas, salidas)

# Mostrar la trama
plt.show()

# Esperar a que se definan los nodos
while len(nodos) == 0:
    nodos = np.array([x.flatten(), y.flatten(), z.flatten()]).T

# Conectar los nodos
for i in range(len(nodos)):
    for j in range(i + 1, len(nodos)):
        if np.linalg.norm(nodos[i] - nodos[j]) < 0.1:
            ax.plot([nodos[i][0], nodos[j][0]], [nodos[i][1], nodos[j][1]], [nodos[i][2], nodos[j][2]], color='red')