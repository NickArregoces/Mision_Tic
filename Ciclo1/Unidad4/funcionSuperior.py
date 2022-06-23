def conversos(sis):
    
    def sis_bin(numero):
        print(f"El numero decimal {numero}, en binario es: {bin(numero)}")
    
    def sis_oct(numero):
        print(f"El numero decimal {numero}, en octal es: {oct(numero)}")
        
    def sis_hex(numero):
        print(f"El numero decimal {numero}, en hexagecimal es: {hex(numero)}")
        
    sisFun = {"bin":sis_bin, "oct": sis_oct, "hex": sis_hex}#UN VALUE QUE LLAMA UNA FUNCION
    return sisFun[sis]

#convertir numero decimal a binario
numeroCon=int(input("Digite un numero: "))#VARIABLE GLOBAL
conversos("oct")(numeroCon)
conversos("hex")(numeroCon)
conversos("bin")(numeroCon)