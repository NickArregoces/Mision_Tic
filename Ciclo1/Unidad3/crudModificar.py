estudiantesActivos={1:["Emilia Rubio"], 2:["Maira Reina"], 3:["Laura Ramirez"], 4:["Andrea Gonzalez"]}

print("Actualizar estudiante")
numeroEstudiante= int(input("Digite el ID del estudiante: "))
estudiantesActivos[numeroEstudiante][0]=str(input("Ingrese el nuevo nombre: "))

print(f"El estudiante: {estudiantesActivos[numeroEstudiante][0]}, ha sido modificado con exito")
print("---------------------------")

def imprimirListadoEstudiante(estudiantes):
    for identificacion, datos in estudiantes.items():
        print(f"el ID de estudiantes es : {identificacion}")
        print(f"El nombre del estudiante es: {datos [0]}") 
        print("-------------------------------------") 

imprimirListadoEstudiante(estudiantesActivos)