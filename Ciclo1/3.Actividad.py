def vel(tiempo: int ,distancia: int ) -> str:
    
    velocidad = distancia   /  tiempo 
    return  "La velocidad es de {} Mestros/segundos ".format(velocidad)

print(vel(4,20))
