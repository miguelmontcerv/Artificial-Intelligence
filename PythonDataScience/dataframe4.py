#Ficheros tipo Excel
## Nota: Se tienen que instalar readxlsx, openpyxl y otras cosas que te vaya pidiendo el instalador 
import pandas as pd 

df = pd.read_excel('Ejemplo_Excel.xlsx')

print(df) #Imprimimos la tabla que tenemos en la carpeta

df['e'] ='12 34 53 15'.split()

writer = pd.ExcelWriter('Salida_Excel.xlsx')
df.to_excel(writer, 'Hoja1', index=False)
writer.save()

print("")
print(df)