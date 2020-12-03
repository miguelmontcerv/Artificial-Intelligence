#RegresionLogistica
# Este programa hace una regresion logisticas (Es decir, nos da valores discretos dado un conjunto de datos)
# Sirve para el spam, cancer, entre otras, este ejemplo nos dice que tipo de sistema operativo utuliza una persona dependiendo del tiempo que tenga en su PC

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import seaborn as sb
#Asignamos el archivo csv al df
dataframe = pd.read_csv(r"usuarios_win_mac_lin.csv")

#Asignamos a X todos los valores menos clase y a Y la clase
X = np.array(dataframe.drop(['clase'],1))
Y = np.array(dataframe['clase'])
#DEfinimos el modelo a utilizar
model = linear_model.LogisticRegression()
#Entrenamos el modelo
model.fit(X,Y)
Y_pr = model.predict(X)
#Imprimimos las predicciones
print(Y_pr)
#Validacion del modelo
cuenta_erroes(Y_pr,Y)
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=0.3, random_state=seed)
predictions = model.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

#Prediccion de nuevos valores
X_new = pd.DataFrame({'duracion': [10], 'paginas': [3], 'acciones': [5], 'valor': [9]})
model.predict(X_new)



def cuenta_erroes(self,Y_pr,Y):
	#Realizamos un programa para ver los haciertos, son 170 datos
	count = 0
	for i in range(170):
	    if Y_pr[i] == Y[i]:
	        count = count + 1
	print(count)
	#Fin programa