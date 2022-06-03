def main():
    print("digite 'si', para continuar el programa")
    respuesta= input("Desea continuar con el programa: ")
    
    while respuesta=="si":
        respuesta= input("Desea continuar con el programa: ")
        
    print("ha terminado el programa")

if __name__=="__main__": #lo utilizo para llamar una funcion que contiene While
    main()      