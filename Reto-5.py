casos = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59,2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
    "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
    "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1] 
#Datos del data set

#Contadores
total_registros = 0
mayores_a_100 = 0
menores = 0
datos_invalidos = 0

#Acumulador
suma_total = 0

#Bandera
datos_con_todas_las_condiciones = False
for dato in casos:
    if dato == "Sin Dato":
        datos_invalidos +=1
    elif int(dato) > 100:
        mayores_a_100 += 1
    else:
        menores +=1
    if dato != "Sin Dato":
        suma_total += dato

    total_registros += 1

if total_registros != 0: #Asignar True en caso de que haya un valor que cumpla todas las condiciones
    datos_con_todas_las_condiciones = True

print("===== RESUMEN ======")
print("Total de registros:", total_registros)
print("Casos mayores a 100:", mayores_a_100)
print("Casos menores:", menores)
print("Casos invalidos:", datos_invalidos)
print("Suma de valores:", suma_total)
print("Existe algun registro que cumpla las condiciones?", datos_con_todas_las_condiciones)