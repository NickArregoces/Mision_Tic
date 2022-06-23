n1=float(input("Por favor ingre el numero 1: "))
n2=float(input("Por favor ingre el numero 2: "))
n3=float(input("Por favor ingre el numero 3: "))

if n1>n2 and n1>n3:
    print (f"el numero mayor es el {n1}")
elif n2>n1 and n2>n3:
    print (f"el numero mayor es el {n2}")
elif n3>n1 and n3>n2:
    print (f"el numero mayor es el {n3}")
else:
    print("Los numero son iguales")