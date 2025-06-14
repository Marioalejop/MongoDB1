"""

Taller de Ejercicios para MongoDB Atlas y Chart
Ejercicio 1: Sensor DHT11 (Temperatura)
Programa que registre lecturas de temperatura con valores como 30°C, 49°C, 35°C usando el sensor DHT11.
{ "sensor": "DHT11", "tipo": "temperatura", "valor": 30, "unidad": "°C" }
{ "sensor": "DHT11", "tipo": "temperatura", "valor": 49, "unidad": "°C" }
{ "sensor": "DHT11", "tipo": "temperatura", "valor": 35, "unidad": "°C" }
Ejercicio 2: Sensor DHT11 (Humedad)
Lecturas de humedad con valores como 50%, 100%, 70% desde un sensor DHT11.
{ "sensor": "DHT11", "tipo": "humedad", "valor": 50, "unidad": "%" }
{ "sensor": "DHT11", "tipo": "humedad", "valor": 100, "unidad": "%" }
{ "sensor": "DHT11", "tipo": "humedad", "valor": 70, "unidad": "%" }
Ejercicio 3: Recorrido de Drone
Simulación del recorrido de un dron registrando distancia y altura en metros (e.g., distancia 30 m, altura 40 m).
{ "vehiculo": "drone", "distancia": 30, "altura": 40, "unidad": "metros" }
{ "vehiculo": "drone", "distancia": 60, "altura": 50, "unidad": "metros" }
Ejercicio 4: Datos de Imagen (Píxeles)
Lecturas de intensidad de píxeles con coordenadas x, y y niveles de gris como valor.
{ "pixel_x": 100, "pixel_y": 200, "valor": 128, "unidad": "nivel gris" }
{ "pixel_x": 110, "pixel_y": 210, "valor": 200, "unidad": "nivel gris" }
Ejercicio 5: Indicadores KPI
Carga de datos de producción para visualizar KPIs como promedio, máximo y mínimo.
{ "tipo": "produccion", "valor": 45 }
{ "tipo": "produccion", "valor": 70 }
{ "tipo": "produccion", "valor": 55 }
Ejercicio 6: Registro de Velocidad
Simulación de velocidad de un robot móvil en km/h.
{ "vehiculo": "robot", "velocidad": 12.5, "unidad": "km/h" }
{ "vehiculo": "robot", "velocidad": 18.2, "unidad": "km/h" }
Ejercicio 7: Nivel de CO2
Lecturas del sensor MQ135 con niveles de calidad del aire en ppm.
{ "sensor": "MQ135", "valor": 450, "unidad": "ppm" }
{ "sensor": "MQ135", "valor": 620, "unidad": "ppm" }
Ejercicio 8: Luz Ambiental (LDR)
Datos de luminosidad con un sensor LDR en unidades de lux.
{ "sensor": "LDR", "valor": 300, "unidad": "lux" }
{ "sensor": "LDR", "valor": 800, "unidad": "lux" }
Ejercicio 9: Consumo Eléctrico
Consumo de energía de dispositivos como computadoras o aires acondicionados en W.
{ "dispositivo": "aire acondicionado", "consumo": 1200, "unidad": "W" }
{ "dispositivo": "computadora", "consumo": 300, "unidad": "W" }
Ejercicio 10: Registro de pH
Mediciones de pH de diferentes soluciones líquidas.
{ "sensor": "pH", "valor": 6.5, "unidad": "pH" }
{ "sensor": "pH", "valor": 7.1, "unidad": "pH" }
Ejercicio 11: Temperatura del Suelo
Lectura de temperatura a nivel del suelo usando un sensor DHT22.
{ "sensor": "DHT22", "valor": 22.5, "unidad": "°C", "nivel": "suelo" }
Ejercicio 12: Cantidad de Pasos
Conteo de pasos diarios por usuario.
{ "usuario": "Laura", "pasos": 3500 }
{ "usuario": "Pedro", "pasos": 7800 }
Ejercicio 13: Presión Atmosférica
Medición de la presión atmosférica en hPa con un sensor BMP180.
{ "sensor": "BMP180", "presion": 1013.25, "unidad": "hPa" }
Ejercicio 14: Nivel del Tanque de Agua
Control del nivel de agua de un tanque medido en porcentaje.
{ "sensor": "ultrasonico", "nivel": 75, "unidad": "%" }
Ejercicio 15: Ritmo Cardíaco
Lectura del ritmo cardíaco en pulsaciones por minuto (BPM).
{ "sensor": "pulso", "bpm": 72 }
{ "sensor": "pulso", "bpm": 88 }
Ejercicio 16: Temperatura Corporal
Registro de temperatura corporal en °C usando termistor.
{ "sensor": "termistor", "valor": 37.8, "unidad": "°C" }
Ejercicio 17: Movimiento con Acelerómetro
Lecturas de aceleración en ejes x, y, z.
{ "sensor": "acelerometro", "eje_x": 0.3, "eje_y": 0.1, "eje_z": 9.8 }
Ejercicio 18: Nivel de Ruido Ambiental
Medición de ruido ambiental en decibeles (dB).
{ "sensor": "microfono", "nivel": 65, "unidad": "dB" }
Ejercicio 19: Uso de CPU
Registro del uso de CPU por núcleo en porcentaje.
{ "cpu": "core 1", "uso": 75, "unidad": "%" }
{ "cpu": "core 2", "uso": 83, "unidad": "%" }
Ejercicio 20: Conteo de Objetos con Cámara
Conteo de objetos detectados por una cámara en movimiento.
{ "sensor": "camara", "objetos_detectados": 3 }

Adicionar , estós datos a los ejercicios que corresponda 
JSON
[
    {
        "sensor": "DHT11",
        "tipo": "temperatura",
        "valor": 30,
        "unidad": "\u00b0C",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "DHT11",
        "tipo": "temperatura",
        "valor": 49,
        "unidad": "\u00b0C",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "DHT11",
        "tipo": "temperatura",
        "valor": 35,
        "unidad": "\u00b0C",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "DHT11",
        "tipo": "humedad",
        "valor": 50,
        "unidad": "%",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "DHT11",
        "tipo": "humedad",
        "valor": 100,
        "unidad": "%",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "DHT11",
        "tipo": "humedad",
        "valor": 70,
        "unidad": "%",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "vehiculo": "drone",
        "distancia": 30,
        "altura": 40,
        "unidad": "metros",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "vehiculo": "drone",
        "distancia": 60,
        "altura": 50,
        "unidad": "metros",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "pixel_x": 100,
        "pixel_y": 200,
        "valor": 128,
        "unidad": "nivel gris",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "pixel_x": 110,
        "pixel_y": 210,
        "valor": 200,
        "unidad": "nivel gris",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "tipo": "produccion",
        "valor": 45,
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "tipo": "produccion",
        "valor": 70,
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "tipo": "produccion",
        "valor": 55,
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "vehiculo": "robot",
        "velocidad": 12.5,
        "unidad": "km/h",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "vehiculo": "robot",
        "velocidad": 18.2,
        "unidad": "km/h",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "MQ135",
        "valor": 450,
        "unidad": "ppm",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "MQ135",
        "valor": 620,
        "unidad": "ppm",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "LDR",
        "valor": 300,
        "unidad": "lux",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "LDR",
        "valor": 800,
        "unidad": "lux",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "dispositivo": "aire acondicionado",
        "consumo": 1200,
        "unidad": "W",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "dispositivo": "computadora",
        "consumo": 300,
        "unidad": "W",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "pH",
        "valor": 6.5,
        "unidad": "pH",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    },
    {
        "sensor": "pH",
        "valor": 7.1,
        "unidad": "pH",
        "timestamp": "2025-06-11T11:59:01.012791-05:00"
    }
]


"""

from pymongo import MongoClient
from urllib.parse import quote_plus
from datetime import datetime
import pytz


# Conectar a MongoDB Atlas
uri = "mongodb+srv://marioalejop:Juliana23@cluster0.xjiaffo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Conectar a la base de datos y colección
db = client["CursoMongoDBTest"]
#coleccion = db["TallerMongoChar"]

# Configurar la zona horaria para Bogotá
timezone = pytz.timezone('America/Bogota')

# Limpiar la colección antes de insertar nuevos datos
colecciones = [db["NivelCO2"],db["Temperatura"],db["Humedad"],db["RecorridoDrone"],db["DatosImagen"],db["IndicadoresKPI"],
               db["Velocidad"],db["LuzAmbiental"],db["ConsumoElectrico"],db["pH"],db["TemperaturaSuelo"],db["CantidadPasos"],
               db["PresionAtmosferica"],db["NivelTanqueAgua"],db["RitmoCardiaco"],db["TemperaturaCorporal"],db["MovimientoAcelerometro"],
               db["NivelRuidoAmbiental"],db["UsoCPU"],db["ConteoObjetosCamara"]]
for coleccion in colecciones:
    coleccion.delete_many({})

# Insertar un dato individual del sensor
"""coleccion.insert_one({
    "sensor": "MQ135",
    "valor": 25,
    "timestamp": datetime.now(timezone),
    "unidad": "ppm",
    "ubicacion": "Laboratorio"
})"""

# db.createCollection("Temperatura") / Manualmente en MongoDB Atlas

# Insertar múltiples lecturas simuladas creando automáticamente las colecciones

db.Temperatura.insert_many([

    #Ejercicio 1: Sensor DHT11 (Temperatura)
    
    { "sensor": "DHT11", "tipo": "temperatura", "valor": 30, "unidad": "\u00b0C", "timestamp": datetime.now(timezone) },
    { "sensor": "DHT11", "tipo": "temperatura", "valor": 49, "unidad": "\u00b0C", "timestamp": datetime.now(timezone) },
    { "sensor": "DHT11", "tipo": "temperatura", "valor": 35, "unidad": "\u00b0C", "timestamp": datetime.now(timezone) }
    
])

db.Humedad.insert_many([

    #Ejercicio 2: Sensor DHT11 (Humedad)

    { "sensor": "DHT11", "tipo": "humedad", "valor": 50, "unidad": "%", "timestamp": datetime.now(timezone) },
    { "sensor": "DHT11", "tipo": "humedad", "valor": 100, "unidad": "%", "timestamp": datetime.now(timezone) },
    { "sensor": "DHT11", "tipo": "humedad", "valor": 70, "unidad": "%", "timestamp": datetime.now(timezone) }
    
])

db.RecorridoDrone.insert_many([

    #Ejercicio 3: Recorrido de Drone

    { "vehiculo": "drone", "distancia": 30, "altura": 40, "unidad": "metros", "timestamp": datetime.now(timezone) },
    { "vehiculo": "drone", "distancia": 60, "altura": 50, "unidad": "metros", "timestamp": datetime.now(timezone) }
])

db.DatosImagen.insert_many([

    #Ejercicio 4: Datos de Imagen (Píxeles)

    { "pixel_x": 100, "pixel_y": 200, "valor": 128, "unidad": "nivel gris", "timestamp": datetime.now(timezone) },
    { "pixel_x": 110, "pixel_y": 210, "valor": 200, "unidad": "nivel gris", "timestamp": datetime.now(timezone) }
])

db.IndicadoresKPI.insert_many([

    #Ejercicio 5: Indicadores KPI

    { "tipo": "produccion", "valor": 45, "timestamp": datetime.now(timezone) },
    { "tipo": "produccion", "valor": 70, "timestamp": datetime.now(timezone) },
    { "tipo": "produccion", "valor": 55, "timestamp": datetime.now(timezone) }
])

db.Velocidad.insert_many([

    #Ejercicio 6: Registro de Velocidad

    { "vehiculo": "robot", "velocidad": 12.5, "unidad": "km/h", "timestamp": datetime.now(timezone) },
    { "vehiculo": "robot", "velocidad": 18.2, "unidad": "km/h", "timestamp": datetime.now(timezone) }
])

db.NivelCO2.insert_many([

    #Ejercicio 7: Nivel de CO2

    { "sensor": "MQ135", "valor": 450, "unidad": "ppm", "timestamp": datetime.now(timezone) },
    { "sensor": "MQ135", "valor": 620, "unidad": "ppm", "timestamp": datetime.now(timezone) }
])

db.LuzAmbiental.insert_many([

    #Ejercicio 8: Luz Ambiental (LDR)

    { "sensor": "LDR", "valor": 300, "unidad": "lux", "timestamp": datetime.now(timezone) },
    { "sensor": "LDR", "valor": 800, "unidad": "lux", "timestamp": datetime.now(timezone) }
])

db.ConsumoElectrico.insert_many([

    #Ejercicio 9: Consumo Eléctrico

    { "dispositivo": "aire acondicionado", "consumo": 1200, "unidad": "W", "timestamp": datetime.now(timezone) },
    { "dispositivo": "computadora", "consumo": 300, "unidad": "W", "timestamp": datetime.now(timezone) }
])

db.pH.insert_many([

    #Ejercicio 10: Registro de pH

    { "sensor": "pH", "valor": 6.5, "unidad": "pH", "timestamp": datetime.now(timezone) },
    { "sensor": "pH", "valor": 7.1, "unidad": "pH", "timestamp": datetime.now(timezone) }
])

db.TemperaturaSuelo.insert_many([

    #Ejercicio 11: Temperatura del Suelo

    { "sensor": "DHT22", "valor": 22.5, "unidad": "°C", "nivel": "suelo", "timestamp": datetime.now(timezone) }
])

db.CantidadPasos.insert_many([

    #Ejercicio 12: Cantidad de Pasos

    { "usuario": "Laura", "pasos": 3500, "timestamp": datetime.now(timezone) },
    { "usuario": "Pedro", "pasos": 7800, "timestamp": datetime.now(timezone) }
])

db.PresionAtmosferica.insert_many([

    #Ejercicio 13: Presión Atmosférica

    { "sensor": "BMP180", "presion": 1013.25, "unidad": "hPa", "timestamp": datetime.now(timezone) }
])

db.NivelTanqueAgua.insert_many([

    #Ejercicio 14: Nivel del Tanque de Agua

    { "sensor": "ultrasonico", "nivel": 75, "unidad": "%", "timestamp": datetime.now(timezone) }
])

db.RitmoCardiaco.insert_many([

    #Ejercicio 15: Ritmo Cardíaco

    { "sensor": "pulso", "bpm": 72, "timestamp": datetime.now(timezone) },
    { "sensor": "pulso", "bpm": 88, "timestamp": datetime.now(timezone) }
])

db.TemperaturaCorporal.insert_many([

    #Ejercicio 16: Temperatura Corporal

    { "sensor": "termistor", "valor": 37.8, "unidad": "°C", "timestamp": datetime.now(timezone) }
])

db.MovimientoAcelerometro.insert_many([

    #Ejercicio 17: Movimiento con Acelerómetro

    { "sensor": "acelerometro", "eje_x": 0.3, "eje_y": 0.1, "eje_z": 9.8, "timestamp": datetime.now(timezone) }
])

db.NivelRuidoAmbiental.insert_many([

    #Ejercicio 18: Nivel de Ruido Ambiental

    { "sensor": "microfono", "nivel": 65, "unidad": "dB", "timestamp": datetime.now(timezone) }
])

db.UsoCPU.insert_many([

    #Ejercicio 19: Uso de CPU

    { "cpu": "core 1", "uso": 75, "unidad": "%", "timestamp": datetime.now(timezone) },
    { "cpu": "core 2", "uso": 83, "unidad": "%", "timestamp": datetime.now(timezone) }
])

db.ConteoObjetosCamara.insert_many([

    #Ejercicio 20: Conteo de Objetos con Cámara
    { "sensor": "camara", "objetos_detectados": 3, "timestamp": datetime.now(timezone) }
])

# Confirmar inserción de datos
print("Los datos fueron insertados correctamente en las colecciones.")

# Mostrar información de las colecciones
for coleccion in colecciones:
    print(f"\nDatos en la colección {coleccion.name}:")
    for doc in coleccion.find():
        print(doc)
    print("\n")