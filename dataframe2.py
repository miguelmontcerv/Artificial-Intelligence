#Seleccion de datos
import numpy as np 
import pandas as pd 

filas = 'ventas1 ventas2 ventas3'.split()
columnas = 'zonaA zonaB zonaC'.split()
datos = [[1,2,3],[4,5,6],[7,8,9]]

df1 = pd.DataFrame(datos,filas,columnas)
print(df1)

condicion = df1 > 4
print("")
print(df1[condicion])

condicion1 = (df1['zonaA'] > 3) & (df1['zonaB'] > 5)
print("")
print(df1[condicion1])

print("")
print(df1[condicion]['zonaB'])

print("")
print(df1)

df1['Dias'] = 'dia1 dia2 dia3'.split()
df1['Horas'] = 'dia1 dia2 dia3'.split()
print("")
print(df1)

df1 = df1.set_index('Dias')
print("")
print(df1)

#df1.dropna() borra columnas donde existan valores nulos
#df1.fillna(value = 100) Llena los valores nulos con algun valor dado, ex = 100

print("")
valor_medio = df1.mean() #Te calcula el promedio por columna
print(valor_medio)