import pandas as pd

df = pd.read_csv("Adquisiciones_realizadas.csv")

print(df.head(5)) # df.head(n) -> Muestra las primeras n filas

print(df.tail(5)) # df.tail(n) -> Muestra las últimas n filas

print(df.columns) # listado de las columnas

print(df.shape) # (filas, columnas)

print(df.info()) # Para cada columna cuántos datos tiene y qué tipo de datos son

print(df.describe()) # Estadística descriptiva

print(df[" Monto_Total_Sin_IVA "]) # df["nombre columna"] Accede a la columna

print(f'Media: {df[" Monto_Total_Sin_IVA "].mean()}') # Media

print(f'Mediana: {df[" Monto_Total_Sin_IVA "].median()}') # Mediana

print(f'Moda: {df["Proveedor"].mode()}') # Moda

print(f'Mínimo: {df[" Monto_Total_Sin_IVA "].min()}') # Mínimo

print(f'Máximo: {df[" Monto_Total_Sin_IVA "].max()}') # Máximo

print(f'Desviación estándar: {df[" Monto_Total_Sin_IVA "].std()}') # Desviación estándar

print(df["Proveedor"].value_counts()) # Tabla de frecuencias