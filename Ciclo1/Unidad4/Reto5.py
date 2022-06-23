import pandas as pd

rutaFileCsv= "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

#split es para separalos
#en la linea 6 es != porque csv es diferente a csv?raw=true
#Head(10) retorna los 10 primeras filas

def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split(".")[-1] != "csv":
        try:
            csv = pd.read_csv(rutaFileCsv)#para leer el csv
            subGrupoPeliculas = csv[["Country", "Language", "Gross Earnings"]]
            gananciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=["Country", "Language"])
            return gananciaPaisLenguaje.head(10)
            
        except:
            print("Error al leer el archivo de datos")
    else:
        print("Extension Invalida")
        
print(listaPeliculas(rutaFileCsv))
