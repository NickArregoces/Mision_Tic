import pandas as pd

inicio = int(input("Por favor ingrese el año incial de las ventas: "))
fin = int(input("Por favor ingrese el año final de las ventas: "))
ventas ={}

for i in range (inicio, fin+1):
    ventas[i]=float(input(f"Ingrese las ventas de {i}: "))

ventas = pd.Series(ventas)
print()
print("Ventas por años \n")
print(f"ventas con descuento \n {ventas*0.9}")
