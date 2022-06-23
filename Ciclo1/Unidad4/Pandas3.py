import pandas as pd

#crear y visualizar un arrays unidimensional como una estructura serie
datos=[1,2,3,4,5]
series= pd.Series(datos)
print(type(datos))
print(type(series))
print(series)


datos1=[1,2,3,4,5]
series1= pd.Series(datos)
print(type(datos1))
print(type(series1))
print(series1)
lista = series1.tolist()#Convertir un objeto serie a lista 
print(type(lista))
print(lista)
print()

#Aplicar las operaciones aritmeticas basicas con objetos series
print("Actividad 5")
serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([6,7,8,9,10])
print(serie1+serie2)
print(serie1-serie2)
print(serie1*serie2)
print(serie1/serie2)

#Aplicar comparaciones con objetos series
print("Actividad 4")
serie1=pd.Series([1,2,3,4,5])
serie2=pd.Series([6,7,8,9,10])
print(serie1<=serie2)
print(serie1>=serie2)
print(serie1==serie2)
print(serie1!=serie2)