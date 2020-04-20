#Graficos de distribucion
import seaborn as sns

propinas = sns.load_dataset('tips') #Datos precargados de la libreria

sns.distplot(propinas['tip'],bins = 30) #Grafica solo un dato

sns.jointplot(x='total_bill',y='tip',data=propinas,kind = 'reg') #Compara solo dos parametros de los datos

sns.pairplot(propinas) #Nos compara unicamente los valores que son cuantificables

sns.pairplot(propinas,hue = 'sex') #Hace lo mismo que arribe pero separa los datos dependiendo de un parametro

#sns.rugplot(propinas['total_bill']) #Nos pinta la cantidad de cada parametro