#Multigraficos

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2,19,10) #Creacion de datos
y = x*2
z = x*(1/x)
w = 1/x

#Figura se tiene de declarar necesariamente
figura, graficos = plt.subplots(nrows = 2, ncols = 2) #Nos general basicamente una matriz de subplots los cuales estan anumerados 0 - n

graficos[0][0].plot(x,y,'blue') #Les damos valores
graficos[0][1].plot(x,z,'green') 
graficos[1][0].plot(y,w,'red') 
graficos[1][1].plot(w,y,'pink') #Se le puede poner en hexa el color así: '#000000'

graficos[0][0].set_title("Azul") #Les ponemos titulo
graficos[0][1].set_title("Verde")
graficos[1][0].set_title("Rojo")
graficos[1][1].set_title("Rosa")

##Dos graficos en un mismo panel
figura3 = plt.figure()
grafico2 = figura3.add_axes([0,0,1,1])
grafico2.plot(x,w**2,label = 'grafico1')
grafico2.plot(x,w**3,label = 'grafico2')
grafico2.legend(loc=0) #Pone la leyenda donde haya espacio

figura2 = plt.figure(figsize=(18,5)) #Cambiar el tamaño de un grafico
grafico = figura2.add_axes([0,0,1,1])
grafico.plot(x,w,'r',linewidth = 5, alpha = 0.7, linestyle = '-',marker = 'x',markersize = 20) #Verificar más estilos de linea en la documentacion de la libreria.
	#El marker nos marca las congruencias en los valores analizados

