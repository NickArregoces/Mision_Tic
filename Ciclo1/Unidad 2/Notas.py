notaAlumno=float(input("Ingrese la nota del estudiante: "))

if notaAlumno <0 or notaAlumno>5:
    print ("La nota no es valida")
elif notaAlumno>=0 and notaAlumno>=3:
    print("Aprobaste")
else:
    print("Reprobado")