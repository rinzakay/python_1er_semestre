import math

# Solicitar las longitudes de los catetos
try:
    a = float(input("Ingrese la longitud del cateto a: "))
    b = float(input("Ingrese la longitud del cateto b: "))

    # Validar que sean positivos
    if a <= 0 or b <= 0:
        print("Error: Las longitudes deben ser números reales positivos.")
    else:
        # Calcular la hipotenusa usando el Teorema de Pitágoras
        c = math.sqrt(a**2 + b**2)

        # Mostrar el valor de la hipotenusa
        print("La hipotenusa es:", c)

        # Determinar el tipo de triángulo
        if a == b:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

except ValueError:
    print("Error: Debe ingresar un número válido.")