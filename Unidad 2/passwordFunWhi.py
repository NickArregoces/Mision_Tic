def main():
    print("CONFIRME SU CONTRASEÑA")
    password = input("Digite su contraseña: ")
    password2 = input("Digite de nuevo su contraseña: ")
    
    while password != password2:
        print ("Las contraseñas son diferentes")
        password = input("Digite su contraseña: ")
        password2 = input("Digite de nuevo su contraseña: ")
        
    print("Contraseña confirmada, ha sido guardada en el sistema")
    
if __name__== "__main__":
    main()