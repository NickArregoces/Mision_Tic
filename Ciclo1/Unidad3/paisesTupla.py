from re import X

def cargarPaisesPoblacion():
    paises=[]
    for x in range(5):
        nombre = input(f"Ingrese el nombre del pais No. {x+1}: ")
        cant = int(input(f"Ingrese la cantidad de habitantes {x+1}: "))
        paises.append((nombre,cant))#esto se convierte a una tupla dentro de una lista
    return paises

def imprimir(paises):
    print("Los paises y su poblacion son :")
    for x in range(0, len(paises)):
        print(paises[x][0],paises[x][1])

def paisMasPoblacion(paises):
    pos=0
    for x in range (0, len(paises)):#len longitud de la lista
        if paises[x][1] > paises [pos][1]:#[x] es la posición de la lista y [1] es la posicion de la tupla
            pos=x
        print(f"pais con mayor cantidad de habitantes es: {paises[pos][0]} con {paises[pos][1]} habitantes") #[0] es el nombre del pais

paises =cargarPaisesPoblacion()
imprimir(paises)
paisMasPoblacion(paises)