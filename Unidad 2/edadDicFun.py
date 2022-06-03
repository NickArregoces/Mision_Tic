nombre=input("Digite su nombre: ")
apellido=input("Digite su apellido: ")
edad=int(input("Digite su  edad: "))

persona={"nombre":nombre, "apellido":apellido, "edad":edad, "año":0}

def edadAlta(persona:dict):
    name= persona["nombre"]
    lastname =persona["apellido"]
    age= persona["edad"]
    year= persona["año"]
    
    if age>=0 and age <18:
        year= 2022 - age
        mayorEdad= year + 18
        return name, lastname, "Eres menor de edad no podemos darte de alta hasta ", mayorEdad
    elif age >18 and age<25:
        return "Tienes un descuento de 10%"
    elif age >25 and age<100:
        return "Los sentimos, no tiene descuento"
    elif age==18 or age==25:
        return "Premio, tienes un descuento especial del 20%"
    elif age <0:
        return "No se puede calcular la edad"
    elif age >=100:
        return "Sigue vivo?"
    else:
        return "Dato no valido"

print(edadAlta(persona))

        