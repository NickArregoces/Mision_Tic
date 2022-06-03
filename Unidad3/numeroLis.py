numeros = []

for i in range (10):
    numero = (int(input(f"Digite los numeros {i+1} del 1 al 10: ")))
    while numero > 10 or numero <= 0:
        print("Por favor digite un numero del 1 al 10")
        numero= (int(input(f"Digite los numeros {i+1} del 1 al 10: ")))
    numeros.append(numero)
    numeros.sort(reverse= True)

print(f"los numero ordenados de mayor a menor son {numeros}")