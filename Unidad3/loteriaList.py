loteria=[]

for i in range(6):
    loteria.append(int(input(f"Digite el numero {i+1} de la loteria: ")))
loteria.sort()#ordenar de menor a mayo
print(f"los numeros ordenado de menor a mayor de la loteria son {loteria}")
loteria.reverse()#el reverse es para poner al contrario de lo que hizo el sort
print(f"los numeros ordenado de mayor a menor de la loteria son {loteria}")

    