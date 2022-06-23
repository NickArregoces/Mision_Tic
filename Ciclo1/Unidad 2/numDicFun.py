def numeros (informacion:dict)->dict():
    a= informacion["n1"]
    b= informacion["n2"]
    c= informacion["n3"]
    
    if a>b and b>c:
        print(f"El orden de los numero de mayor a menor es: {a}, {b}, {c}")
    elif a>c and c>b:
        print(f"El orden de los numero de mayor a menor es: {a}, {c}, {b}")
    elif b>a and a>c:
        print(f"El orden de los numero de mayor a menor es: {b}, {a}, {c}")
    elif b>c and c>a:
        print(f"El orden de los numero de mayor a menor es: {b}, {c}, {a}") 
    elif c>a and a>b:
        print(f"El orden de los numero de mayor a menor es: {c}, {a}, {b}")
    elif c>b and b>a:
        print(f"El orden de los numero de mayor a menor es: {c}, {b}, {a}")
    else:
        print("Algunos de los numeros son iguales")

n1=int(input("Ingrese el numero 1: "))
n2=int(input("Ingrese el numero 2: "))
n3=int(input("Ingrese el numero 3: "))
informacion= {"n1":n1,"n2":n2,"n3":n3}
numeros(informacion)
