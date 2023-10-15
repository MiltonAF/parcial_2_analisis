def interpolacion_lagrange(X, Y, X_valor):
    # Asegurémonos de que los datos tengan la misma longitud
    if len(X) != len(Y):
        return "Los datos de entrada no tienen la misma longitud."

    n = len(X)
    resultado = 0.0

    for i in range(n):
        termino = Y[i]
        for j in range(n):
            if j != i:
                termino *= (X_valor - X[j]) / (X[i] - X[j])
        resultado += termino

    return resultado

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

# Realizar la interpolación de Lagrange
resultado = interpolacion_lagrange(X, Y, X_valor)

# Tabular el resultado
tabla = f"| X   | Y (Conocido) | Y (Estimado) | Diferencia |\n"
tabla += f"|-----|------------|------------|------------|\n"
for i in range(len(X)):
    tabla += f"| {X[i]:.2f} | {Y[i]:.2f} | {Y[i]:.2f} | {0:.2f} |\n"
tabla += f"| {X_valor:.2f} | {'':.2f} | {resultado:.2f} | {'':.2f} |\n"

print(tabla)
