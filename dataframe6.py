#Guardar datos en una base de datos SQL
##instalar sqlalchemy
import pandas as pd 
from sqlalchemy import create_engine

diccionario = {'A':[1,2,3], 'B':[4,5,6]}
df = pd.DataFrame(diccionario)

engine = create_engine('sqlite:///:memory:')

df.to_sql('Tabla1',engine,index = False)

datos_leidos_bd = pd.read_sql('Tabla1', con = engine)

print(datos_leidos_bd)