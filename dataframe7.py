#Graficos
import numpy as np 
import pandas as pd 

df = pd.DataFrame(np.random.randint(200,size = (50,4)),columns = ['a','b','c','d'])

df['a'].hist() #Genera un histograma que no es visible en la terminal :(

df['b'].hist(bins = 30) #El histograma tendra 30 columnas

df['c'].plot.hist() #Otra forma de imprimir la tabla

df['d'].plot.area(alpha = 0.3) #Imprime las areas de valores de cada columna, alpha modifica la transparentibilidad de la grafica y mejor diseño

df['a'].plot.bar() #Grafica de barras

df.plot.scatter(x='a',y='b')