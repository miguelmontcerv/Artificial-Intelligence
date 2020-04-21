#Conceptos basicos de un data frame
import numpy as np
import pandas as pd

filas = ['ventas1','ventas2','ventas3']
columnas = ['zonaA','zonaB','zonaC']
datos = [[1,2,3],[4,5,6],[7,8,9]]

df1 = pd.DataFrame(datos,filas,columnas)
print("\n"+str(df1))

print("")

print(df1.loc[ ['ventas1','ventas3'] ])
print("")
print( df1['zonaB'] )

print("\nVenta 1, zonaC: ")
print( df1.loc['ventas1']['zonaC'] )

df1['TotalZonas'] = df1['zonaA'] + df1['zonaB'] +df1['zonaC']
print("\n")
print( df1)

print("\n")
print( df1.drop('TotalZonas',axis = 1) )

print("\n")
df1.drop('TotalZonas',axis = 1,inplace = True)
print(df1)

print("Hola gh")

print("")
df1.drop('ventas3',inplace = True)
print(df1)

print("")
print(df1.shape)
