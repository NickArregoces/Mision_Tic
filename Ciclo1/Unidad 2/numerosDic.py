n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
numeros={"a": n1, "b":n2}

if numeros["a"]== numeros["b"]:
    print (f"Los numeros", numeros["a"], numeros["b"]," son igaules")
elif numeros["a"] > numeros["b"]:
    print (f"El numero", numeros["a"], "es mayor que",numeros["b"])
else:
    print (f"El numero", numeros["a"], "es menor que",numeros["b"])