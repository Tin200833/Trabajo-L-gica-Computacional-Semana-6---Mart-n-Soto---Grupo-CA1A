casos = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59,2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
    "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
    "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1,""] 
#Datos del data set

#Contadores
datos_validos = 0
mayores_a_100 = 0
menores = 0
datos_invalidos = 0

#Acumulador
suma_total = 0

#Banderas
bandera_datos_invalidos = False
bandera_datos_validos = False
bandera_datos_menores = False
bandera_datos_mayores_a_100 = False

for dato in casos:
    if dato == "Sin Dato" or dato == "":
        datos_invalidos += 1
        bandera_datos_invalidos = True #Cambiar a True cuando se encuentre un dato invalido
    else:
        datos_validos += 1
        bandera_datos_validos = True #Cambiar a True cuando se encuentre un dato válido
        suma_total += dato
        if dato > 100:
            mayores_a_100 += 1
            bandera_datos_mayores_a_100 = True #Cambiar a True cuando se encuentre un dato mayor a 100
        else:
            menores += 1
            bandera_datos_menores = True #Cambiar a True cuando se encuentre un dato que no cumpla la condición anterior

print("Total de registros:", datos_validos)
print("Casos mayores a 100:", mayores_a_100)
print("Casos menores:", menores)
print("Casos invalidos:", datos_invalidos)
print("Suma de valores:", suma_total)
print("¿Existe algún dato que cumpla con la condición datos_invalidos?", bandera_datos_invalidos)
print("¿Existe algún dato que cumpla con la condición datos_validos?", bandera_datos_validos)
print("¿Existe algún dato que cumpla con la condición mayores_a_100?", bandera_datos_mayores_a_100)
print("¿Existe algún dato que cumpla con la condición menores?", bandera_datos_menores)