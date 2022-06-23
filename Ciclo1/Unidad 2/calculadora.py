n1=float(input("Digite el primer valor: "))
n2=float(input("Digite el segundo valor: "))

operacion= input("Elija la operacion que deseada: S=suma, R=restas, M=multiplicación, D=division\n") .upper()

if operacion=="S":
    suma=n1+n2
    print(f"La suma de los numeros es: {suma}")
elif operacion=="R":
    resta=n1-n2
    print(f"La resta de los numeros es: {resta}")
elif operacion=="M":
    multiplicacion=n1*n2
    print(f"La multiplicacion de los numeros es: {multiplicacion}")
elif operacion=="D":
    if n2!=0 :
        division=n1/n2
        print(f"La division de los numeros es: {division}")
    else:
        print("El divisor no puede ser 0")
else:
    print("Incorrecto")