'''FLOAT = FLOTANTES (SON NÚMEROS DECIMALES EJ: 32.45)
SE PUEDEN USAR PARA MEDIR LA ESTATURA DE UNA PERSONA
'''

# DECLARANDO 2 VARIABLES TIPO ENTEROS (INT)
# No podemos comenzar un número entero por 0
edad = 18
año_de_nac = 2006

# IMPRESIÓN DE VARIABLES
print(edad)
print("Hola, tengo", edad, "años y nací en el año", año_de_nac)

# DECLARANDO 2 VARIABLES TIPO FLOTANTE (FLOAT)
estatura = 1.56
peso = 65.7

# IMPRESIÓN DE LAS VARIABLES
# Los números en coma flotante son números con decimales (números reales en PSeInt)
print("Mi estatura es", estatura, "m y mi peso es", peso, "kg")

# NÚMEROS COMPLEJOS (COMPLEX)
complejo = 4 + 5j  # se está declarando un número complejo
comp = complex(8, 12)  # otra forma de declarar un número complejo

# Ingresado por consola 
# Ojo: al ingresar por consola, se debe escribir con la forma 5+2j por ejemplo
complejo_ingresado = complex(input("Ingrese un número complejo (ej: 3+4j): "))
print("El número complejo ingresado es:", complejo_ingresado)

# IMPORTAR EL MÓDULO math PARA ACCEDER A pi
import math

# Asignar el valor de pi desde math
pi = math.pi

# FORMATEANDO LA SALIDA DE LOS NÚMEROS
# Forma 1
print("El valor de pi es aproximadamente {:.2f}".format(pi))

# Forma 2
print(f"El valor de pi es aproximadamente: {pi:.2f}")

# Forma 3
print("La velocidad del objeto en caída libre es de:", "%.2f" % pi)

