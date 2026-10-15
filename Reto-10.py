#Definir funciones
def es_dato_completo(valor):
    if valor is None:
        return False
    texto = str(valor).strip()
    if texto == "":
        return False
    if texto.lower() in ["sin dato", "na", "n/a", "nan", "none"]:
        return False
    else:
        return True


def es_edad_valida(edad):
    if not str(edad).isdigit():
        return False
    if int(edad) < 0 or int(edad) > 120:
        return False
    else:
        return True


def es_rango_valido(texto):
    texto = str(texto).strip().lower()
    if texto.startswith("mayor de"):
        numero = texto[8:].strip()
        return es_edad_valida(numero)
    if texto.startswith("menor de"):
        numero = texto[8:].strip().split(" ")[0]
        return es_edad_valida(numero)
    partes = texto.split(" a ")
    if len(partes) != 2:
        return False 
    inicio = partes[0].strip()
    fin = partes[1].strip()
    if not es_edad_valida(inicio) or not es_edad_valida(fin):
        return False
    if int(inicio) > int(fin):
        return False
    else:
        return True


def es_codigo_valido(codigo):
    codigo = str(codigo).strip()
    if " - " not in codigo:
        return False
    prefijo = codigo.split(" - ")[0]
    if len(prefijo) != 2 or not prefijo.isdigit():
        return False
    if int(prefijo) < 1 or int(prefijo) > 21:
        return False
    else:
        return True


def es_categoria_valida(categoria, categorias_validas):
    if categoria in categorias_validas:
        return True
    else:
        return False


def esta_en_rango(valor, minimo, maximo):
    if not str(valor).isdigit():
        return False
    valor = int(valor)
    if valor < minimo or valor > maximo:
        return False
    else:
        return True


def es_numero_valido(numero):
    if not str(numero).isdigit():
        return False
    else:
        return True

#Llamar todas las funciones creadas para crear una función que permita validar un registro completo   
def es_registro_valido(registro):
    if not es_codigo_valido(registro.get("LOCALIDAD_RESIDENCIA")):
        return False
    if not es_rango_valido(registro.get("GRUPOS_EDAD")):
        return False
    if not es_categoria_valida(registro.get("SEXO"), ["M", "F"]):
        return False
    if not esta_en_rango(registro.get("ESTRATO_SOCIOECONOMICO"), 1, 6):
        return False
    if not es_numero_valido(registro.get("CASOS")):
        return False
    if not es_numero_valido(registro.get("MUERTES")):
        return False
    else:
        return True

#Usar la función anterior para procesar cada registro
def procesar_registros(lista_registros):
    validos = []
    invalidos = []
    posicion = 0
    for registro in lista_registros:
        posicion += 1
        if es_registro_valido(registro):
            print("Registro", posicion, "-> Válido")
            validos.append(registro)
        else:
            print("Registro", posicion, "-> Inválido")
            invalidos.append(registro)

    print("Total de registros:", len(lista_registros))
    print("Registros válidos:", len(validos))
    print("Registros inválidos:", len(invalidos))
    return validos, invalidos

registros = [
    {"LOCALIDAD_RESIDENCIA": "09 - Fontibón", "GRUPOS_EDAD": "45 A 49",
     "SEXO": "M", "ESTRATO_SOCIOECONOMICO": 2, "CASOS": 2, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "15 - Antonio Nariño", "GRUPOS_EDAD": "40 a 44",
     "SEXO": "F", "ESTRATO_SOCIOECONOMICO": 6, "CASOS": 1, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "04 - San Cristóbal", "GRUPOS_EDAD": "55 a 59",
     "SEXO": "M", "ESTRATO_SOCIOECONOMICO": 2, "CASOS": 424, "MUERTES": 16},
    {"LOCALIDAD_RESIDENCIA": "11 - Suba", "GRUPOS_EDAD": "20 a 24",
     "SEXO": "M", "ESTRATO_SOCIOECONOMICO": "Sin Dato", "CASOS": 443, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "Sin Dato", "GRUPOS_EDAD": "80 a 84",
     "SEXO": "F", "ESTRATO_SOCIOECONOMICO": 2, "CASOS": 2, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "06 - Tunjuelito", "GRUPOS_EDAD": "Mayor de 100",
     "SEXO": "F", "ESTRATO_SOCIOECONOMICO": 3, "CASOS": 2, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "10 - Engativá", "GRUPOS_EDAD": "10 a 14",
     "SEXO": "X", "ESTRATO_SOCIOECONOMICO": 5, "CASOS": 3, "MUERTES": 0},
    {"LOCALIDAD_RESIDENCIA": "08 - Kennedy", "GRUPOS_EDAD": "5 a 9",
     "SEXO": "F", "ESTRATO_SOCIOECONOMICO": 3, "CASOS": -4, "MUERTES": 0},
]

#Crear una función que permita hacer un resumen completo
def generar_resumen(validos, invalidos):
    total = len(validos) + len(invalidos)

    cantidad_por_sexo = {}
    for registro in validos:
        sexo = registro["SEXO"]
        if sexo in cantidad_por_sexo:
            cantidad_por_sexo[sexo] += 1
        else:
            cantidad_por_sexo[sexo] = 1

    suma_casos = 0
    suma_muertes = 0
    bandera_hay_muertes = False
    for registro in validos:
        suma_casos += int(registro["CASOS"])
        suma_muertes += int(registro["MUERTES"])
        if int(registro["MUERTES"]) > 0:
            bandera_hay_muertes = True

    bandera_hay_invalidos = len(invalidos) > 0

    if total > 0:
        porcentaje_invalidos = len(invalidos) / total * 100
    else:
        porcentaje_invalidos = 0

    if suma_casos > 0:
        tasa_mortalidad = suma_muertes / suma_casos * 100
    else:
        tasa_mortalidad = 0

    print("===== RESUMEN =====")
    print("Total de registros:", total)
    print("Registros válidos:", len(validos))
    print("Registros inválidos:", len(invalidos))
    print("Porcentaje de registros inválidos:", porcentaje_invalidos , "%")
    print("Cantidad por sexo (válidos):")
    for sexo in cantidad_por_sexo:
        print(sexo, "->", cantidad_por_sexo[sexo])
    print("Suma de casos (válidos):", suma_casos)
    print("Suma de muertes (válidos):", suma_muertes)
    print("Tasa de mortalidad:", round(tasa_mortalidad, 2), "%")
    print("¿Existe algún registro válido con muertes?", bandera_hay_muertes)
    print("¿Existe algún registro inválido?", bandera_hay_invalidos)


validos, invalidos = procesar_registros(registros)
generar_resumen(validos, invalidos)