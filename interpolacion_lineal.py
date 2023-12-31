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

# Solicitar al usuario los valores conocidos
X = []
Y = []
num_puntos = int(input("Ingrese el número de puntos conocidos: "))

for i in range(num_puntos):
    x = float(input(f"Ingrese el valor de X_{i + 1}: "))
    y = float(input(f"Ingrese el valor de Y_{i + 1}: "))
    X.append(x)
    Y.append(y)

# Valor a interpolar
X_valor = float(input("Ingrese el valor de X para interpolar: "))

# Realizar la interpolación lineal
resultado = interpolacion_lineal(X, Y, X_valor)

# Tabular el resultado
tabla = f"| X   | Y (Conocido) | Y (Estimado) | Diferencia |\n"
tabla += f"|-----|------------|------------|------------|\n"
for i in range(len(X)):
    tabla += f"| {X[i]:.2f} | {Y[i]:.2f} | {Y[i]:.2f} | {0:.2f} |\n"
tabla += f"| {X_valor:.2f} | {'':.2f} | {resultado:.2f} | {'':.2f} |\n"

print(tabla)
