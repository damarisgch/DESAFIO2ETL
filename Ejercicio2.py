"""
Ejercicio 2: Conectarse a un archivo Excel y extraer datos utilizando la librería pandas
Dado un archivo Excel llamado "datos.xlsx" con una hoja llamada "Sheet1" que contiene datos
similares al ejercicio anterior, escribe un programa en Python que lea el archivo, almacene
los datos en un DataFrame y muestre los resultados
"""
import pandas as pd
archivo_excel = "D:\CursoQualesDP\DESAFIO2ETL\datos.xlsx"
# Carga el archivo Excel en un DataFrame
df = pd.read_excel(archivo_excel, sheet_name="Sheet1")

print(df.head())
