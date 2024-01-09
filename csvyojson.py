import csv
import json
import sys

#Obtener argumentos de linea de comandos
argumentos = sys.argv
comandos = argumentos[1:]

# Leer el archivo CSV y crear un diccionario para almacenar los datos
def getCsvData(csv_path):
    datos = {}
    with open(csv_path, 'r') as csv_file: #lee el archivo csv
        csv_reader = csv.DictReader(csv_file) #Extrae la informacion del csv en forma de objeto
        for row in csv_reader: #Extrae la informacion del objeto y lo convierte a un lista
            for header, value in row.items():
                if header not in datos:
                    datos[header] = []
                datos[header].append(value)
    return datos

def setJsonFile(json_path, datos):
    # Escribir los datos en formato JSON en el archivo de salida
    with open(json_path, 'w') as json_file:
        json.dump(datos, json_file, indent=4)

print("Archivo JSON creado exitosamente.")
