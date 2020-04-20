#Agrupacion de datos
import numpy as np 
import pandas as pd 

diccionario = {'dias':['dia1','dia1','dia2','dia2','dia3','dia3'], 'vendedores':['Ana', 'Mike','Lalo','Juan','Pedro','Mary'], 'ventas':[100,300,150,200,220,140], 'comicion':[50,150,75,100,110,70]}
diccionario2 = {'dias':['dia1','dia1','dia2','dia3'], 'vendedores':['Ana', 'Mike','Lalo','Mary'], 'ventas':[100,200,220,140], 'comicion':[50,100,110,70]}
df = pd.DataFrame(diccionario)
df2 = pd.DataFrame(diccionario2)
print(df)

grp1 = df.groupby('dias').mean()
print("")
print(str(grp1))

grp1 = df.groupby('dias').sum()
print("")
print(str(grp1))

grp1 = df.groupby('dias').describe()
print("")
print(str(grp1))

#Concatenacion de datos

print("")
print( pd.concat([df,df2]) ) #Se crean más columnas (hacia abajo)

print("")
print( pd.concat([df,df2], axis = 1)) #Se crean más filas (hacia la izquierda)

print("")
print( pd.merge(df,df2, on ='ventas')) #Junta las dos tablas a partir de una fila igual en ambas, sino sale algo raro como a mi

print("")
#print( df.join(df2) ) Junta a partir de la primer fila.

print(df['vendedores'].unique()) #Nos regresa un array donde los valores son unicos

print("")
print(df['vendedores'].nunique()) #Nos regresa el numero de valores son unicos

print("")
print(df['vendedores'].value_counts()) #Nos regresa el numero de incurrencias de cada valor en la fila

print("")
print(df['ventas'].apply(lambda x: x*2)) #Nos regresa el numero de incurrencias de cada valor en la fila

print("")
print(df.sort_values('ventas')) #Acomoda de menor a mayor una fila (no cambia los indices, solo los reacomda para la impresion)

