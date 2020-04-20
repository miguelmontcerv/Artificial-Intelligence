#Graficos de distribucion
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

propinas = sns.load_dataset('tips')

#sns.barplot(x = 'sex', y = 'total_bill', data = propinas) #Funcion comparadora

#sns.countplot(x = 'sex',data = propinas) #Muestra la cantidad de un parametro

#sns.boxplot(x = 'day', y = 'total_bill', data = propinas)

#sns.stripplot(x = 'day', y = 'total_bill', data = propinas, hue = 'sex') #Con puntos encimados por categoria

#sns.swarmplot(x = 'day', y = 'total_bill', data = propinas, hue = 'sex') #Con puntos no encimados por categoria

##### Mapas de calor #####

#vuelos = sns.load_dataset('flights')
#vuelos_matriz = vuelos.pivot_table(index = 'month',columns = 'year',values = 'passengers')

#sns.heatmap(vuelos_matriz)

#### pairGrid y FacetGrid ####
flores = sns.load_dataset('iris')

#sns.pairplot(flores)

graficos = sns.PairGrid(flores) #Nos genera la combinacion de valores en graficos sin formato
#graficos.map(plt.scatter) #generalizamos el tipo de grafico
graficos.map_diag(sns.distplot)
graficos.map_upper(plt.scatter)
graficos.map_lower(sns.kdeplot)

graficos2 = sns.FacetGrid(data =propinas,col = 'time',row = 'smoker') #A partir de las combinaciones de estas columnas
graficos2.map(sns.distplot,'total_bill') #Grafica este dato

