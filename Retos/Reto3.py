# Inicializamos la lista para guardar los números
numeros = []

# Obtenemos los números del 500 al 100, disminuyendo de 3 en 3
for i in range(500, 99, -3):
    numeros.append(i)

# Imprimimos los números obtenidos
print("Números obtenidos:")
print(numeros)

# Calculamos la suma de todos los números
suma_total = sum(numeros)

# Calculamos el promedio
promedio = suma_total / len(numeros)

# Mostramos los resultados en consola
print(f"\nSuma total de los números: {suma_total}")
print(f"Promedio de los números: {promedio:.2f}")