def muv(velocidad: float, tiempo: float ) -> str:
        
    tiempoMinutos = tiempo * (1/60)
    
    distancia = velocidad * tiempoMinutos
     
    return  "La distancia que la motocicleta recorrio es de: {}km ".format(distancia,)

print(muv(120,55))
 