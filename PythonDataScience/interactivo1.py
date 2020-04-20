#Modulos Plotly y Cufflinks
import pandas as pd
import numpy as np 
import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(conected = True)

cf.go_offline()

#%matplotlib inline

df = pd.DataFrame(np.random.randn(100,4),columns = ['a','b','c','d'])