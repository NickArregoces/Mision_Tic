saldo=1000

while True:
    print("\t Menu")#centrar titulo
    print("1: Ingresar dinero a la cuenta")
    print("2: Retirar dinero de la cuenta")
    print("3: Mostrar el saldo disponible")
    print("4: Salir")

    opcion=int(input("Digite la opcion del menu: "))


    if opcion==1:
        cantidad = float(input("cuanto dinero desea ingresar: "))
        saldo += cantidad # saldo+cantidad
        print(f"Su nuevo saldo es: {saldo}")
    elif opcion==2:
        retirar=float(input("Cuanto desea retirar: "))
        if retirar > saldo:
            print("No tienes fondos suficientes")
        else:
            saldo-= retirar
            print(f"Su nuevo saldo es: {saldo}")
    elif opcion==3:
        print(f"Su saldo es: {saldo}")

    elif opcion==4:
        print("Gracias por utilizar nuestros servicios")
        break #termina el bucle
    else:
        print("Opcion no valida")

