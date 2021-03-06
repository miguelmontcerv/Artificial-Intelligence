# 2.4 cbind, rbind, manipulaci�n de DF 

# Funci�n cbind

# La funci�n cbind toma una sucesi�n de argumentos que pueden ser 
# vectores, matrices o data frames y los combina por columnas, 
# por ejemplo 

cbind(1:10, 11:20, 21:30)
cbind(1:10, matrix(11:30, ncol =2))
cbind(data.frame(x = 1:10, y = 11:20), z = 21:30)

# Funci�n rbind

# La funci�n rbind funciona de manera similar a cbind, pero en lugar 
# de combinar los objetos por columnas, los combina por filas, como
# ejemplo tenemos lo siguiente

df1 <- data.frame(x = 1:5, y = 6:10, z = 16:20)
df2 <- data.frame(x = 51:55, y = 101:105, z = 151:155)
(df1); df2
rbind(df1, df2)