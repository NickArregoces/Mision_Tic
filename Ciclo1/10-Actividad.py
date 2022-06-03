def dinero(guillermo: int) -> str:
        
    luis = guillermo / 2
    
    juan = (guillermo + luis) / 2
    
    total = guillermo + luis + juan

    return "El todal de dinero de los tres es de: {}$".format(total)

print(dinero(1000000)) 

