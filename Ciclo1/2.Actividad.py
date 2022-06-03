def convertidor(segundos: int )-> str:
    
    minutos = segundos // 60
    return "Es {} minutos ".format(minutos)

print(convertidor(60)) 