casos = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59
] #Datos del data set

#Contadores de mayor y menor a 100
casos_mayores = 0
casos_menores = 0

for caso in casos:
    if caso > 100:
        print(caso, "Cumple la condición: -> True")
        casos_mayores += 1
    else:
        print(caso, "No cumple la condición: -> False")
        casos_menores += 1

print("Número de casos mayores a 100 (Cumplen la condición):", casos_mayores)
print("Número de casos menores o iguales a 100 (No cumplen la condición):", casos_menores)