#Lab de pseint pasado a python

# Solicitar datos al usuario
precio_unitario = float(input("Ingrese el precio unitario del libro: "))
cantidad = int(input("Ingrese la cantidad de libros a comprar: "))
es_academico = input("¿Es un libro académico? (Si/No): ").strip().capitalize()
es_afiliado = input("¿Está afiliado/a a la Universidad de Los Lagos? (Si/No): ").strip().capitalize()

# Calcular subtotal
subtotal = precio_unitario * cantidad

# Descuento por libro académico (15%)
if es_academico == "Si":
    descuento_academico = subtotal * 0.15
else:
    descuento_academico = 0

total_despues_academico = subtotal - descuento_academico

# Descuento por afiliación ULagos (5%)
if es_afiliado == "Si":
    descuento_afiliado = total_despues_academico * 0.05
else:
    descuento_afiliado = 0

total_despues_afiliado = total_despues_academico - descuento_afiliado

# Descuento por volumen de compra (5% si total supera $50.000)
if total_despues_afiliado > 50000:
    descuento_volumen = total_despues_afiliado * 0.05
else:
    descuento_volumen = 0

# Total final a pagar
total_final = total_despues_afiliado - descuento_volumen

# Total descuentos aplicados
total_descuentos = descuento_academico + descuento_afiliado + descuento_volumen

# Mostrar resultados
print("\n----- RESUMEN DE COMPRA -----")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento por libro académico: ${descuento_academico:.2f}")
print(f"Descuento por afiliación: ${descuento_afiliado:.2f}")
print(f"Descuento por volumen: ${descuento_volumen:.2f}")
print(f"Total de descuentos: ${total_descuentos:.2f}")
print(f"Total a pagar: ${total_final:.2f}")
