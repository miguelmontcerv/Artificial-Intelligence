#Graficos
import numpy as np 
import pandas as pd 

df = pd.DataFrame(np.random.randint(200,size = (50,4)),columns = ['a','b','c','d'])

#df['a'].hist() #Genera un histograma que no es visible en la terminal :(

#df['b'].hist(bins = 30) #El histograma tendra 30 columnas

#df['c'].plot.hist() #Otra forma de imprimir la tabla

#df.plot.area(alpha = 0.3) #Imprime las areas de valores de cada columna, alpha modifica la transparentibilidad de la grafica y mejor diseño

#df.plot.bar(stacked = True) #Barras con apilamiento

#df['a'].plot.bar() #Grafica de barras

#df.plot.scatter(x='a',y='b')

#df.plot.scatter(x='a',y='b',c='c',cmap = 'coolwarm')

#df.plot.box()

#df.plot.hexbin(x = 'a',y = 'b',gridsize = 15) #El tamaño esta 'invertido' entre más grande, menor sera

#df.plot.kde()

df.plot.density() #Hace un grafico igual al de arriba