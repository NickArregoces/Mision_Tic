from errno import ESTALE


estudiantesActivos={1:["Emilia Rubio"], 2:["Maira Reina"], 3:["Laura Ramirez"], 4:["Andrea Gonzalez"]}

def numeroEstudiante(estudiantes,nombreEstudiante):
    for identificacion, nombre in estudiantes.items():
        if nombre[0].lower() == nombreEstudiante.lower():
            return identificacion
    return 0

def imprimirListadoEstudiante(estudiantes):
    for identificacion, datos in estudiantes.items():
        print(f"el ID de estudiantes es : {identificacion}")
        print(f"El nombre del estudiante es: {datos [0]}") 
        print("-------------------------------------") 
print("Eliminar informacion")

eliminarEstudiante =int(input("Digite el ID del estudiante: "))
if eliminarEstudiante in estudiantesActivos:
    nombreEstudiante= estudiantesActivos[eliminarEstudiante][0]
    eliminarEstudiante=numeroEstudiante(estudiantesActivos, nombreEstudiante)
    del estudiantesActivos[eliminarEstudiante]
    print(f"El estudiante {nombreEstudiante} ha sido eliminado")
    imprimirListadoEstudiante(estudiantesActivos)
else:
    print("El estudiante no se encuentra")