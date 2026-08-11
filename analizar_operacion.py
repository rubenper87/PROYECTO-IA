import csv
with open("datos_operacion.csv", newline="", encoding="utf-8") as archivo:
    datos = list(csv.DictReader(archivo))

with open("historico_eventos.csv", newline="", encoding="utf-8") as archivo:
    historico = list(csv.DictReader(archivo))
print("REGISTRO DE OPERACIÓN")
print("-" * 30)

for registro in datos:
    print(
        registro["fecha"],
        registro["hora"],
        "| Presión:", registro["presion"],
        "| Temperatura:", registro["temperatura"],
        "| Caudal:", registro["caudal"],
        "| Estado:", registro["estado"]
    )
    presion_inicial = float(datos[0]["presion"])
presion_final = float(datos[-1]["presion"])

cambio_presion = presion_final - presion_inicial

print()
print("ANÁLISIS DE TENDENCIA")
print("-" * 30)
print("Cambio de presión:", cambio_presion)

if cambio_presion >= 10:
    print("⚠️ Atención: la presión presenta una tendencia ascendente significativa.")
else:
    print("La presión no presenta una tendencia ascendente significativa.")
    temperatura_inicial = float(datos[0]["temperatura"])
temperatura_final = float(datos[-1]["temperatura"])
temperatura_inicial = float(datos[0]["temperatura"])
temperatura_final = float(datos[-1]["temperatura"])
caudal_inicial = float(datos[0]["caudal"])
caudal_final = float(datos[-1]["caudal"])

cambio_temperatura = temperatura_final - temperatura_inicial
cambio_caudal = caudal_final - caudal_inicial

print()
print("ANÁLISIS CONJUNTO")
print("-" * 30)
print("Cambio de presión:", cambio_presion)
print("Cambio de temperatura:", cambio_temperatura)
print("Cambio de caudal:", cambio_caudal)

if cambio_presion >= 10 and cambio_temperatura <= -10 and cambio_caudal <= -10:
    print("⚠️ Atención: se observa una evolución conjunta de presión, temperatura y caudal.")
else:
    print("No se observa una combinación significativa de las tres variables.")
print()
print("ANTECEDENTES HISTÓRICOS")
print("-" * 30)

for evento in historico:
    print(
        evento["fecha"],
        "|", evento["tipo_evento"],
        "| Causa:", evento["causa"],
        "| Solución:", evento["solucion"]
    )
    print()
print("EVENTOS SIMILARES")
print("-" * 30)

for evento in historico:
    diferencia_presion = abs(float(evento["presion"]) - presion_final)
    diferencia_caudal = abs(float(evento["caudal"]) - caudal_final)

    if diferencia_presion <= 5 and diferencia_caudal <= 5:
        print(
            "Fecha:", evento["fecha"],
            "| Evento:", evento["tipo_evento"],
            "| Causa:", evento["causa"],
            "| Solución:", evento["solucion"]
        )
        mejor_evento = None
mejor_puntuacion = None
for evento in historico:
    diferencia_presion = abs(float(evento["presion"]) - presion_final)
    diferencia_caudal = abs(float(evento["caudal"]) - caudal_final)

    puntuacion = diferencia_presion + diferencia_caudal

    if mejor_puntuacion is None or puntuacion < mejor_puntuacion:
        mejor_puntuacion = puntuacion
        mejor_evento = evento
print()
print("CASO HISTÓRICO MÁS PARECIDO")
print("-" * 30)

print(
    "Evento:", mejor_evento["tipo_evento"],
    "| Causa:", mejor_evento["causa"],
    "| Solución:", mejor_evento["solucion"]
)
print()
print("=" * 50)
print("INFORME AUTOMÁTICO DE OPERACIÓN")
print("=" * 50)

print()
print("SITUACIÓN DETECTADA")
print("La presión presenta una tendencia ascendente mientras")
print("la temperatura y el caudal disminuyen.")

print()
print("ANTECEDENTE MÁS PARECIDO")
print("Evento:", mejor_evento["tipo_evento"])
print("Causa:", mejor_evento["causa"])
print("Actuación registrada:", mejor_evento["solucion"])

print()
print("RECOMENDACIÓN")
print("Revisar las condiciones de operación y valorar las")
print("medidas aplicadas en el antecedente histórico.")

print()
print("NOTA: La recomendación debe ser validada por el operador.")