#Tercera clase de arreglos: 
import numpy as np

array1 = np.random.rand(4,3)
print(str(array1)+"\n")

array2 = np.random.randn(4,3) #Con numero negativos
print(str(array2)+"\n")

array3 = np.random.randint(1,51,50) #Con numero positivos, pero solo son unidimencionales los arreglos
print(str(array3)+"") #Nos muestra un vector de 25 elementos de entre 1 - 50
num = array3.max()
num2 = array3.argmax()
print("El maximo numero es "+str(num)+" y esta en "+str(num2))
num = array3.min()
num2 = array3.argmin()
print("El minimo numero es "+str(num)+" y esta en "+str(num2)+"\n")

array3 = array3.reshape(5,10) #El reajuste de elementos siempre debe de dar exactamente igual que la cantidad de elementos del arreglo mayor
print(str(array3)+"\n")

array3 = array3.reshape(10,5)
print(str(array3)+"\n") 