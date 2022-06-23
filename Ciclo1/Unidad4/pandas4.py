import pandas as pd

def resumenCotizacion(fichero):
    df = pd.read_csv(fichero, sep=";" , decimal=",", thousands=".",  index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=["valor Minimo", "valor Maximo", "valor Promedio"])

print(resumenCotizacion("D:/Descargas/Mision Tic/Unidad4/cotizacion.csv"))
