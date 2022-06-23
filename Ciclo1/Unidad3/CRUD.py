
#paso 1: crear diccionario con datos ya creados
estudiantesActivos={1:["Emilia Rubio"], 2:["Maira Reina"], 3:["Laura Ramirez"], 4:["Andrea Gonzalez"]}
#Se usan [] por la salida con el .tem

#paso 2: pedir informacion del usuario
print("cargar estudiantes")
identificacionEstudiante=int(input("Digite el ID del estudiante: "))
nombreEstudiante=str(input("Digite el nombre del estudiante: "))

#paso 3: argar funciones de carga estudiante e imprimir listado total
def cargarEstudiante(identificacion: int, nombre:str):#en los parametros debo llamarlo diferente pero similar
    estudiantesActivos[identificacion]=[nombre]
    print("informacion cargada con exito")
    return estudiantesActivos

#imprimir listado de estudiantes
def imprimirListadoEstudiantes(estudiantes):#en los parametros debo llamarlo diferente pero similar
    estudiantesActivos=estudiantes
    for identificacion, datos in estudiantes.items():#El items es para no imprimir con "" y separe los datos del diccionario
        print(f"el ID de estudiantes es : {identificacion}")
        print(f"El nombre del estudiante es: {datos [0]}") 
        print("-------------------------------------") 
              

estudiantesActivos=cargarEstudiante(identificacionEstudiante,nombreEstudiante)
#paso 4 invocar la funcion
imprimirListadoEstudiantes(estudiantesActivos)