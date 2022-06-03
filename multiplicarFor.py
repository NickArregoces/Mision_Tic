numero= int (input("Digite la tabla de multiplicar: "))

for i in range(1,11):#comienza en 1 hasta 10
    resultado= numero*i
    print(f"{numero} X {i} = {resultado}")