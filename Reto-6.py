casos = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59,2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
    "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
    "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1] 
#Datos del data set donde ninguno cumple con la condición

registros_totales = 0
bandera = False
for caso in casos:
    if caso == 0 or caso == "":
        bandera = True
    registros_totales += 1

print(bandera)
    
#La bandera no cambia ya que al iterar en todos los datos no hay ninguno que cumpla las condiciones.

