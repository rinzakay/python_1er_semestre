from colorama import init, Fore
init()

print(Fore.GREEN + "#### 01- CONDICIONALES IF, ELSE, ELIF ####")

licencia = input("¿Tienes licencia de conducir?: (Si) o (No)").lower()
edad = int(input("Ingresa tu edad: "))
automovil = input("¿Tienes automóvil?: (Si) o (No)").lower()

print(Fore.YELLOW + "## Testeando comparadores y el IF ##")

# Verificar licencia
if licencia == "si":
    print("Puedo conducir porque tengo licencia")
else:
    print("No tengo licencia para conducir")

# Verificar edad
if edad >= 18:
    print("Puedo conducir porque soy mayor de edad")
else:
    print("No puedo conducir porque no soy mayor de edad")

# Verificar combinación de licencia y edad
if licencia == "si" and edad >= 18:
    print("Puedo conducir porque tengo licencia y la edad suficiente")
elif licencia == "si" and edad < 18:
    print("No puedo conducir porque, aunque tengo licencia, no tengo la edad")
else:
    print("No puedo conducir porque no cumplo con los requisitos")

# Verificar además si tiene auto
if licencia == "si" and edad >= 18 and automovil == "si":
    print("Puedo conducir porque tengo licencia, edad y automóvil")
else:
    print("No cumplo con todos los requisitos para conducir un automóvil propio")
