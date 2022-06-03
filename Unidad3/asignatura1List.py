asignaturas = ["matematicas","fisicas","quimica","historia","lengua"]
aprobado = []
for asignatura in asignaturas:#Imprime cada elemento de la lista
    nota=float(input(f"Digita la nota de {asignatura}: "))
    
    while nota > 5 or nota < 0:
        print ("ingrese una nota entre 0 y 5")
        nota=float(input(f"Digita la nota de {asignatura}: "))
    else: #Se utiliza else con while cuando sigue un if   
        if nota >=3:
            aprobado.append(asignatura)#agrego en aprobado las asignaturas
print("Ha terminado de digitar las notas")

for asignatura in aprobado:
    asignaturas.remove(asignatura)
if len(asignaturas) == 0:#si la lista esta vacia
    print("Paso todas las materias")
else:    
    print(f"tiene que repetir {asignaturas}")
