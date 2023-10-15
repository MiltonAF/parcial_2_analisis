import numpy as np
from sklearn.linear_model import LinearRegression

# Datos conocidos: Tiempo (min) y Temperatura (°C)
X = np.array([0, 20, 40]).reshape(-1, 1)  # Tiempo
Y = np.array([100, 80, 60])  # Temperatura

# Valor a interpolar
X_valor = 30

# Crear un modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, Y)

# Estimar Y para el valor X_valor
Y_estimado = modelo.predict(np.array([[X_valor]]))[0]

# Tabular el resultado
tabla = f"| X   | Y (Conocido) | Y (Estimado) | Diferencia |\n"
tabla += f"|-----|------------|------------|------------|\n"
for i in range(len(X)):
    tabla += f"| {X[i][0]:3} | {Y[i]:11} | {Y[i]:11} | {0:11} |\n"
tabla += f"| {X_valor:3} | {'':11} | {Y_estimado:11.2f} | {'':11} |\n"

print(tabla)
