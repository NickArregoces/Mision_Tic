import pandas as pd

s = pd.Series({"Matematicas":3.5, "Historia":3.3,"Economia":4.0,"Programacion":3.6,"Ingles":4.5}, dtype="string")#series= lista y diccionarios
print(s)

print(s[1:3])#valores 1 y 2 de la series
print(s["Historia"])#print value
print(s[["Matematicas","Ingles"]])