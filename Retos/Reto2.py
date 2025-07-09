#Definir el inventario con frutas y sus precios
Inventario = {
    "Manzana": (800,750,820),
    "Platano": (500,500,600), #Dos precios iguales y uno diferente
    "Cereza": (1200,1250,1230)
    }

#Obtener precios únicos del plátano usando un set 
precios_platano = set(Inventario["Platano"])

#Crear una lista con los tipos de frutas
tipos_frutas = list(Inventario.keys())

#Calcular el promedio de los precios únicos del plátano
promedio_platano = sum(precios_platano) /3
len(precios_platano)

#Mostrar resultados
print("Inventario completo:")
print(Inventario)

print("\nPrecios únicos del plátano:")
print(precios_platano)

print("\nTipos de frutas:")
print(tipos_frutas)

print(f"\nPromedio de precios únicos del plátano):{promedio_platano:3f}")