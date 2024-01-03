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

# Encontrar los nodos
nodos = np.array([x.flatten(), y.flatten(), z.flatten()]).T

# Conectar los nodos
for i in range(len(nodos)):
    for j in range(i + 1, len(nodos)):
        if np.linalg.norm(nodos[i] - nodos[j]) < 0.1:
            ax.plot([nodos[i][0], nodos[j][0]], [nodos[i][1], nodos[j][1]], [nodos[i][2], nodos[j][2]], color='red')

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

# Entrenar la red
entradas = np.random.rand(len(nodos), 100)
salidas = np.random.randint(0, 2, size=(len(nodos), 100))
for i in range(100):
    entrenamiento(entradas, salidas)

# Cargar los datos de entrada
entradas_iris = np.loadtxt('iris.csv', delimiter=',')

# Normalizar los datos de entrada
entradas_iris = (entradas_iris - np.mean(entradas_iris, axis=0)) / np.std(entradas_iris, axis=0)

# Dividir los datos de entrada en conjuntos de entrenamiento y prueba
entradas_iris_train, entradas_iris_test = np.split(entradas_iris, [int(0.8 * len(entradas_iris))])

# Obtener las etiquetas de salida
salidas_iris_train = entradas_iris_train[:, -1]
salidas_iris_test = entradas_iris_test[:, -1]

# Eliminar las etiquetas de salida de los datos de entrada
entradas_iris_train = entradas_iris_train[:, :-1]
entradas_iris_test = entradas_iris_test[:, :-1]

# Entrenar la red con los datos de entrenamiento
entrenamiento(entradas_iris_train, salidas_iris_train)

# Evaluar la red con los datos de prueba
salidas_iris_pred = funcion_activacion(np.dot(entradas_iris_test, pesos))
salidas_iris_pred = np.argmax(salidas_iris_pred, axis=1)
accuracy = np.mean(salidas_iris_pred == salidas_iris_test)
print('Accuracy:', accuracy)

# Mostrar la trama
plt.show()