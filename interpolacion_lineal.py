def interpolacion_lineal(X, Y, X_valor):
    # Asegurémonos de que los datos tengan la misma longitud
    if len(X) != len(Y):
        return "Los datos de entrada no tienen la misma longitud."

    # Encuentra los puntos más cercanos en X
    for i in range(len(X) - 1):
        if X[i] <= X_valor <= X[i + 1]:
            X1, X2, Y1, Y2 = X[i], X[i + 1], Y[i], Y[i + 1]
            break
    else:
        return "El valor X no está dentro del rango de datos conocidos."

    # Realiza la interpolación lineal
    Y_valor = Y1 + (X_valor - X1) * (Y2 - Y1) / (X2 - X1)

    return Y_valor

# Datos conocidos: Tiempo (min) y Temperatura (°C)
X = [0, 20, 40]
Y = [100, 80, 60]

# Valor a interpolar
X_valor = 30

# Realizar la interpolación lineal
resultado = interpolacion_lineal(X, Y, X_valor)

# Tabular el resultado
tabla = f"| X   | Y (Conocido) | Y (Estimado) | Diferencia |\n"
tabla += f"|-----|------------|------------|------------|\n"
for i in range(len(X)):
    tabla += f"| {X[i]:3} | {Y[i]:11} | {Y[i]:11} | {0:11} |\n"
tabla += f"| {X_valor:3} | {'':11} | {resultado:11.2f} | {'':11} |\n"

print(tabla)