#Fichero html
## Se debe instalar lxml
import numpy as np 
import pandas as pd 

pagina_web = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'

datos = pd.read_html(pagina_web) #Nos regresa una lista de elementos

df = datos[0]

print(df.head(10))