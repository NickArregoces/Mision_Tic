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

