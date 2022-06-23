
asignaturas = ["matematicas","fisicas","quimica","historia","lengua"]
notas = []
for asignatura in asignaturas:#Imprime cada elemento de la lista
    nota=float(input(f"Digita la nota de {asignatura}: "))
    notas.append(nota)#.append() es para agregar cada input en orden de la lista
print("Ha terminado de digitar las notas")

for i in range (len(asignaturas)):# range(en el rango de la lista ) len(la longitud de la lista)
    print(f"En el curso {asignaturas[i]} has sacado la calificacion {notas[i]}")
    
