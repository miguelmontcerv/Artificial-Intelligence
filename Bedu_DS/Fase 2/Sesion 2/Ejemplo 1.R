# 2.1 Medidas de Tendencia Central, de Posici�n y de Dispersi�n

# Medidas de Tendencia Central

# En R utilizamos la funci�n mean para calcular la media de un conjunto de
# mediciones, por ejemplo

x = c(4000, 9000, 9000, 10000);
mean(x) #Media o promedio

# Para calcular la mediana, utilizamos la funci�n median, por ejemplo

median(x) #Mediana

# Si lo que deseamos es obtener la moda de un conjunto de mediciones, una 
# alternativa es instalar el paquete DescTools en R mediante la instrucci�n
# install.packages("DescTools"), luego utilizamos la funci�n Mode del paquete
# DescTools

library(DescTools)
Mode(x) # mode es diferente de Mode (Case sensitive)

# Medidas de Posici�n

# En R utilizamos la funci�n quantile para obtener cuantiles muestrales. Por
# ejemplo

x <- c(29, 13, 62, 4, 63, 96, 1, 90, 50, 46)

quantile(x, 0.25) # cuantil del 25%
quantile(x, c(0.25,0.50,0.75)) # Cuartiles
quantile(x, seq(0.1,0.9, by = 0.1)) # Deciles

# Medidas de Dispersi�n

# Podemos calcular el rango intercuart�lico en R con la funci�n IQR, 
# por ejemplo,

IQR(x)

# o bien

quantile(x, probs = 0.75) - quantile(x, probs = 0.25)

# La varianza y desviaci�n est�ndar muestral en R las calculamos con las 
# siguientes instrucciones respectivamente

var(x)
sd(x)
