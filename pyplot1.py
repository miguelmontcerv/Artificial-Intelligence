#Primer programa de matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2,9,10)
y = x*2

plt.title("Primer Grafico")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.plot(x,y,'red') #Grafica de forma sencilla

plt.subplot(2,1,1)
plt.plot(x,y,'green')

plt.subplot(2,1,2)
plt.plot(x,y,'blue')

#Progrmacion Orientada a Objetos

figura = plt.figure()

grafico = figura.add_axes([0,0,1,1]) #Los valores van del 0 a 1, los primeros dos son las cordenadas y los otros el tamaño x,y
grafico.plot(x,y,'red')

#grafico = figura.add_axes([0.5,0.5,0.5,0.5]) #Los valores van del 0 a 1
#grafico.plot(x,y,'green')

grafico2 = figura.add_axes([0.2,0.1,0.3,0.3])
grafico2.plot(y,x,'green')