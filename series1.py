import numpy as np 
import pandas as pd 

etiquetas = ['venta1','venta2','venta3']
datos = [1,2,3]

serie1 = pd.Series(data = datos, index = etiquetas)
print(serie1)
print(serie1['venta3'])