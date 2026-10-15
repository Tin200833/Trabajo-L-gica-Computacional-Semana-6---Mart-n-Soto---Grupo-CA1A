casos = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59
] #Datos del data set

suma_valores = 0
for caso in casos:
    suma_valores += caso #Sumar el valor anterior con el siguiente valor del data set

print("Suma de los valores:", suma_valores)