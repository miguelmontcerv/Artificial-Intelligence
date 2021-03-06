# Ejemplo 3. Listas y data frames

# Objetivo
# Crear listas y data frames
# Extraer informaci�n de estos
# C�lculo de estad�sticos b�sicos

# Requisitos

# Prework
# R, RStudio
# Ejemplos 1 y 2

# Desarrollo

# Seguir el contenido y tratar de comprender el c�digo mostrado a continuaci�n

# Listas

(milista <- list(nombre = "Pepe", no.hijos = 3, edades.hijos = c(4, 7, 9)))

# propiedades de la lista

str(milista)

# Extrayendo elementos de la lista, recuerda que para ingresar se debe usar el s�mbolo $

z <- milista$edades.hijos
mean(z)
# Creando data frames

x <- 6:8
y <- c("A", "B", "C")
(mifile <- data.frame(edad = x, grupo = y))

str(mifile)

# Extrayendo informaci�n del df, se hace igual que con las matrices

mifile[1]
mifile[,2]
mifile$edad

# Calculando algunos estad�sticos b�sicos

mean(mifile$edad)

# Podemos hacer uso de la funci�n `paste` para agregar un mensaje

paste("La media de la edad es:", mean(mifile$edad))

# Podemos inspeccionar a detalle el df utilizando `summary`

summary(mifile)

# Tambi�n se puede conocer su dimensi�n

dim(mifile)

# Podemos agregar una columna extra con datos

mifile$sexo <- c("H", "M", "H")
mifile

# Si fuera el caso, se puede eliminar una columna

mifile$sexo <- NULL
mifile
