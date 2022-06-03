edad= int(input("Digite la edad: "))

if edad > 0 and edad <=90:
    print("su numero es valido")
    if edad>=18:
        print ("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("La edad no es valida")