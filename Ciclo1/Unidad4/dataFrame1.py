import pandas as pd
import numpy as np

#Obtener las primeras n filas  de un DataFrame
nombre=["Sebastian","Alonso","Elena","Helena","Lizeth","Loraine","Maria"]
puntaje =[11.5,8,15.5,18,22.3,10,11]
intentos=[1,2,4,7,5,6,8]
califico=["si","no","no","si","si","si","si"]
indices =["A","B","C","D","E","F","G"]
jugadores={"nombre":nombre, "puntaje":puntaje,"intentos":intentos,"califico":califico}

df = pd.DataFrame(data=jugadores, index = indices)
print(df)
print(df.iloc[:3])
print(df.iloc[-3:])#las ultimas 3 filas
print()
#obtener los ejes(atributo de filas y columnas) 
print(df.axes)
#Seleccionar filas y columnas especificas de un DataFrame con iloc
print()
print(df.iloc[[1,4],[0,3]])

#obtener dimension,tamaño y forma de un DataFrame
print()
print(df.size)
print(df.ndim)
print(df.shape)

#Mostrar la memory que ocupa el DataFrame
print(df.memory_usage())
