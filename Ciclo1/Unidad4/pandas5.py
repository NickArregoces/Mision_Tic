import pandas as pd

#Convertir un diccionario en un objeto serie
print("Actividad 6")
dicc = {"A":10,"B":20,"C":30}
serie = pd.Series(dicc)
print(serie)
print(serie["A"])

#Convertir un NumYy en un objeto serie
print("Actividad 7")
import numpy as np 
arreglo =np.array([1,2,3,4,5,6])
print(arreglo)
serieArr = pd.Series(arreglo)
print(serieArr)
print()

#Cambiar el tipo de datos en un objeto Series
print("Actividad 8")
datos = pd.Series(["100","200","300","Sailor Moon","300.15","He-man"])
datos = pd.to_numeric(datos,errors="coerce")#convertir los datos a numericos, y los string como no definido
print(datos)
print()

#Obtener una columna de un objeto DataFrame como un Objeto serie
print("Actividad 9")
datosDic ={"a":[1,2,3,4,5], "B":[5,6,7,8,9],"C":[2,7,10,11,12]}
df = pd.DataFrame(data=datosDic)
print(df)
columna = df.iloc[:,0]#iloc es para obtener inf de un dataframe
print(columna)#[:,0]extraer la columna a
print()
fila = df.iloc[3,:]#extraer  fila 3
print(fila)

print (df.iloc[3,1])
print (df.iloc[:,0:2])#imprime las dos columnas
