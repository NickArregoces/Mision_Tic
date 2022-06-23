import pandas as pd

#convertir series con multiples lista en una unica serie
print("actividad 11")
datos =[["Colombia","Peru","Brazil","Argentina"],["Ecuador","Mexico"],["Chile"]]
serie=pd.Series(datos)
print(serie)
serie=serie.apply(pd.Series).stack().reset_index(drop=True)
print(serie)
print()
#Ordenar los valores de una series con el metodo sort_values
print("actividad 12")
datosOrd=["1.1.","20","30","0.5","Panda","Java"]
serieOrd = pd.Series(datosOrd)
serieOrd = pd.Series(serieOrd).sort_values()
print(serieOrd)
print()

#Agregar elemento a series existentes
print("actividad 13")
serieOrd = serieOrd.append(pd.Series(["JavaScript","HTML"])).reset_index(drop=True)
print(serieOrd)
 