def convertidor(pies: int, pulgadas: float)-> str: 
    
    cm = pies * 30.48
    cm  += pulgadas * 2.54

    return "la conversion en centImetros es de : {}cm".format(cm)

print(convertidor( 10 , 5 ))