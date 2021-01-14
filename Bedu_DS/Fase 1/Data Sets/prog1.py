import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns

vinos = pd.read_csv('vino.csv')
vinos.head()

vinos['Wine Type'].value_counts()

#Graficamos los datos de este set
sns.pairplot(vinos,hue = 'Wine Type')
