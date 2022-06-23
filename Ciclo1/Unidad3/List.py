nombre=["Nicolas", "Andres","Michel", "cosita","sebastian"]
print(nombre[0])
print(nombre[-1])
print(nombre[-5])
print(nombre[1:4])

#dimension de la lista
print(len(nombre))

#cambiar elementos de la lista
nombre[3]="Nohemy"
print(nombre)

#Verificar si esta en la lista
if "Michel" in nombre:
    print("Si esta en la lista")
else:
    print("No esta en la lista")
#iterar una lista
for nombres in nombre:
    print(nombres)

#Agregar un nombre a lista
nombre.append("Ronald")
print(nombre)

#Agregar nombre donde yo desee
nombre.insert(2,"Maira")
print(nombre)

#Remover elemento de la lista
nombre.remove("Maira")
print(nombre)

#Remover sin saber como se llama el ultimo elemento
nombre.pop()
print(nombre)

del nombre[1]
print (nombre)

#nombre.clear(): quitar todos los elementos