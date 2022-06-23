import pandas as pd
notas = { "Juan":0,"Camila":0, "Elena":0,"Loraine":0,"Laura":0,"Maira":0}

for keys in notas:
    notas[keys] = float(input(f"Digite la nota del estudiante {keys}: "))

print(notas)    

def estadisticasNotas(notas):
    notas=pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ["Notas minima", "Notas maxima", "Nota promedio","Desviacion tipica"])
    return estadisticos

print(estadisticasNotas(notas))