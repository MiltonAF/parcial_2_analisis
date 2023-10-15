def diferencias_divididas(x, y):
    n = len(x)
    coeficientes = []

    # Crear una matriz de diferencias divididas
    matriz_diferencias = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matriz_diferencias[i][0] = y[i]

    # Calcular las diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            matriz_diferencias[i][j] = (matriz_diferencias[i + 1][j - 1] - matriz_diferencias[i][j - 1]) / (x[i + j] - x[i])

    # Obtener los coeficientes del polinomio
    for i in range(n):
        coeficientes.append(matriz_diferencias[0][i])

    return coeficientes

def interpolacion_newton(x, y, x_valor):
    coeficientes = diferencias_divididas(x, y)
    n = len(coeficientes)
    resultado = coeficientes[0]

    for i in range(1, n):
        producto = coeficientes[i]
        for j in range(i):
            producto *= (x_valor - x[j])
        resultado += producto

    return resultado

# Datos conocidos: Tiempo (min) y Temperatura (°C)
X = [0, 20, 40]
Y = [100, 80, 60]

# Valor a interpolar
X_valor = 30

# Realizar la interpolación de Newton
resultado = interpolacion_newton(X, Y, X_valor)

# Tabular el resultado
tabla = f"| X   | Y (Conocido) | Y (Estimado) | Diferencia |\n"
tabla += f"|-----|------------|------------|------------|\n"
for i in range(len(X)):
    tabla += f"| {X[i]:3} | {Y[i]:11} | {Y[i]:11} | {0:11} |\n"
tabla += f"| {X_valor:3} | {'':11} | {resultado:11.2f} | {'':11} |\n"

print(tabla)
