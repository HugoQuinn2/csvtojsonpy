import csv
import json
import sys
import os

#Obtener argumentos de linea de comandos
argumentos = sys.argv
comandos = argumentos[1:]

# Leer el archivo CSV y crear un diccionario para almacenar los datos
def getCsvData(csv_path):
    datos = {}
    nombre, extension = os.path.splitext(csv_path)
    if extension.lower() == '.csv':
        with open(csv_path, 'r') as csv_path: #lee el archivo csv
            csv_reader = csv.DictReader(csv_path) #Extrae la informacion del csv en forma de objeto
            for row in csv_reader: #Extrae la informacion del objeto y lo convierte a un lista
                for header, value in row.items():
                    if header not in datos:
                        datos[header] = []
                    datos[header].append(value)
    return datos

def setJsonFile(json_path, datos):
    # Escribir los datos en formato JSON en el archivo de salida
    with open(json_path + '.json', 'w') as json_file:
        json.dump(datos, json_file, indent=4)

def getCsvFiles():
    archivos_csv = []
    for archivo in os.listdir('./'):
        if archivo.endswith('.csv'):
            archivos_csv.append(archivo)
    return archivos_csv

def main():
    if len(comandos) > 0:
        for file in comandos:
            nombre, ext = os.path.splitext(file)
            if ext.lower() == '.csv':
                datos = getCsvData(file)
                setJsonFile(nombre, datos)
    else:
        csv_files = getCsvFiles()
        for file in csv_files:
            datos = getCsvData(file)
            nombre, ext = os.path.splitext(file)
            setJsonFile(nombre, datos)

if __name__ == "__main__":
    main()



