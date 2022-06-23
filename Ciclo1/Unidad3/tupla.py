frutas=("naranja","mango","banano")
print(frutas)

print(len(frutas))
print(frutas[1])
print(frutas[-1])
#fruta[0]="kiwi"#una TUPLA ES INMUTABLE, NO SE PUEDE MODIFICAR

#modificando tupla
frutaLista= list(frutas)
frutaLista[0]="kiwi"
frutas = tuple(frutaLista)
print (frutas)
################

#iterar una tupla es un FOR
for fruta in frutas:
    print(fruta, end ='/ ')#para que el for imprima horizontal
