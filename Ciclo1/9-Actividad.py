def empleado(horas: int, salarioHora: float) -> str:
        
    salario = horas * salarioHora

    return  "El salario semanal es: {}".format(salario)

print(empleado(10,10)) 