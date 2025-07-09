#Diccionario
gatos = {
    101: {"Nombre": "Luna", "Peso": 1.2, "Edad": 3, "Tamaño": 30},
    102: {"Nombre": "Michi", "Peso": 0.8, "Edad": 2, "Tamaño": 25},
    103: {"Nombre": "Pepito", "Peso": 2.5, "Edad": 14, "Tamaño": 35}
    }

print ("Gatos:")
print (gatos)

#Recorrido con un Bucle
for num in gatos:
    p = gatos[num]["Peso"]
    if p <1:
        clasificacion = "Bajo peso"
    elif p <=4:
        clasificacion = "Normal"
    else: 
        clasificacion = "Sobre peso"


#Bucle de la edad
for num in gatos:
    try:
        edad = gatos[num]["Edad"]
        if edad < 4:
            categoria = "Cachorro"
        elif edad <= 12:
            categoria = "Joven"
        else:
            categoria = "Adulto"
        gatos[num]["Categoria"] = categoria
    except:
        gatos[num]["Categoria"] = "Desconocida"

#Tupla mayor a menor
lp = []
for num in gatos:
    lp.append((num, gatos[num]["Peso"]))

lp.sort()

print("\nLista ordenada: ")
print(lp)

#Bucle datos de nuevos gatos
continuar = "s"
while continuar == "s":
    nuevo_num = int(input("\nNúmero de ingreso: "))
    nombre = input("Nombre: ")
    peso = float(input("Peso: "))
    edad = int(input("Edad: "))
    tamaño = int(input("Tamaño: "))
    gatos[nuevo_num] = {"Nombre": nombre, "Peso": peso, "Edad": edad, "Tamaño": tamaño}
    continuar = input("¿Desea agregar otro gatito? (s/n): ")

#Modificación de tamaño
num_modificar = int(input("\nNúmero de ingreso para cambiar tamaño: "))
if num_modificar in gatos:
    nuevo_tamaño = int(input("Nuevo tamaño: "))
    gatos[num_modificar]["Tamaño"] = nuevo_tamaño
else:
    print("No existe ese número.")

#Calculo
pesos = []
for num in gatos:
    pesos.append((num, gatos[num]["Peso"]))

#Promedio
suma = 0
for p in pesos:
    suma += p[1]
promedio = suma / len(pesos)

#Mayor y menor peso
mayor = pesos[0]
menor = pesos[0]
for p in pesos:
    if p[1] > mayor[1]:
        mayor = p
    if p[1] < menor[1]:
        menor = p

print("\nPromedio de pesos:", promedio)
print("Mayor peso:", mayor)
print("Menor peso:", menor)
print("Número de ingreso con menor peso:", menor[0])

#Diccionario final ordenado
print("\nDiccionario final de gatos:")
for num in sorted(gatos):
    print(num, gatos[num])
