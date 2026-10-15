registros = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59,2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
    "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
    "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1,""] 

for registro in registros:
    contador = 0
    if registro != 0:
        contador += 1

print(contador) # Da 0, ya que al interar en cada dato, el contador se reinicia a 0 ya que está dentro del ciclo. 

#Código corregido:
registros = [
    2, 1, 424, 101, 1, 4, 2, 39, 3, 443,
    1, 6, 240, 37, 1, 1, 1, 2, 2, 2,
    3, 2, 1, 94, 2, 3, 13, 1, 1, 59,2, 6, 2, 3, 6, 2, 3, 1, 5, "Sin Dato", 2, 2, 3, 6, 3,
    "Sin Dato", "Sin Dato", 4, 2, 2, 5, 6, 4, "Sin Dato",
    "Sin Dato", 2, 5, 5, 4, 2, 3, "Sin Dato", 4, 3, 1,""] 

contador = 0 #Inicializar el contador fuera del ciclo para que vaya guardando la información al iterar cada dato.
for registro in registros:
    if registro != 0:
        contador += 1

print(contador) #Al colocar el contador antes del ciclo este no se reinicia al iterar cada dato, por lo que va guardando información.