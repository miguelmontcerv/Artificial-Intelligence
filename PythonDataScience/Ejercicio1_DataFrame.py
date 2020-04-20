#Ejercicio

#Crear lista "Asignaturas" con los valores "Matematicas,fisica,historia"
#Hacer otra lista con las tres notas
#Hacer una serie con "Asignaturas" como indice
#Crear una variable con la nota fisica y acceder a ella para imprimir el dato

import pandas as pd

Asignaturas = ['Matematicas', 'Fisica','Historia']
Notas = ['9','9','8']

serie = pd.Series(data = Notas, index = Asignaturas)

calificacion_fisica = serie['Fisica']

print("La calificacion es "+str(calificacion_fisica))