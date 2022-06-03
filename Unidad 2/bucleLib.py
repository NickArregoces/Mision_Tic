#blucle positivo raiz 
import math#libreria matematica

num = int(input("Digite el numero: "))

while num < 0:
    print("El numero ingresado es negativo")
    num = int(input("Debe registrar un numero postivio: "))

print(f"la raiz cuadrada es: {(math.sqrt(num)): .4f}") #4f es para mostrar 4 decimales   