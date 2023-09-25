"""
Ejercicio 1: Conexión y Extracción de Datos desde un Archivo CSV.
Dado un archivo CSV llamado "datos.csv" con la siguiente estructura:
Nombre,Edad,Ciudad
Alice,28,New York
Bob,32,Los Angeles
Carol,45,Chicago
Escribe un programa en Python que lea el archivo, almacene los datos en un DataFrame y
muestre los resultados por pantalla.
"""

import pandas as pd
datos = pd.read_csv('D:\CursoQualesDP\DESAFIO2ETL\datos.csv',header = None)
print(datos)

