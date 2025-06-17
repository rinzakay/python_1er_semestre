# Definir la función que cuenta cuántas veces aparece 'a'
def contar_a(frase):
    return frase.lower().count('a')

# A. Ingresar una frase de máximo 30 caracteres
frase = input("Ingresa una frase de máximo 30 caracteres: ")[:30]

# Llamar a la función y mostrar el resultado
print("Cantidad de letras 'a':", contar_a(frase))