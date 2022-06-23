meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

salir=False
while(not salir):#True
    
    numero = int(input("Digite un numero: "))
    
    if (numero==0):
        salir=True
    else:
        if(numero>=1 and numero <=len(meses)):
            print(meses[numero-1])# se resta para ubicarlo en la tupla que esta inicia en 0
        else:
            print(f"Digite un numero 1 y {len(meses)}")