#Estratos del data set
estratos = [2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
            "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
            "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1]

numero_de_estratos = 0
datos_sin_dato = 0
for estrato in estratos:
    if estrato == "Sin Dato":
        datos_sin_dato += 1
    else:
        numero_de_estratos += 1

print("Número de estratos:", numero_de_estratos)
print("Número de datos sin dato:", datos_sin_dato)
print("Número total de elementos:", len(estratos))