# A) Crear diccionario con datos
datos = {
    5700000: {"Ciudad": "Castro", "Temperatura": 11.8, "Precipitacion": 2000},
    5770000: {"Ciudad": "Chonchi", "Temperatura": 8.3, "Precipitacion": 2800},
    5790000: {"Ciudad": "Quellón", "Temperatura": 10.2, "Precipitacion": 2950}
}

print(datos)

# B) Agregar clave "Clima"
for c in datos:
    try:
        t = datos[c]["Temperatura"]
        if t < 10:
            datos[c]["Clima"] = "Frío"
        elif t <= 15:
            datos[c]["Clima"] = "Templado"
        else:
            datos[c]["Clima"] = "Cálido"
    except:
        datos[c]["Clima"] = "Desconocida"

print(datos)

# C) Agregar meses a Castro
datos[5700000]["Meses"] = []
datos[5700000]["Meses"].append("Mayo")
datos[5700000]["Meses"].append("Junio")
datos[5700000]["Meses"].append("Julio")
datos[5700000]["Meses"].pop(1)

print(datos)

# D) Cambiar nombre Chonchi
datos[5770000]["Ciudad"] = "Ciudad de los Tres Pisos"

print(datos)

# E) Lista de precipitaciones y cálculos
lluvias = [datos[5700000]["Precipitacion"], datos[5770000]["Precipitacion"], datos[5790000]["Precipitacion"]]

print(sum(lluvias))
print(max(lluvias))
print(min(lluvias))
print(lluvias.index(max(lluvias)))

# F) Imprimir diccionario final
print(datos)

# G) Lista de tuplas
tuplas = list(datos.items())
print(tuplas)
