class Persona: #Funciones Superiores
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "{} tiene {} años " .format(self.nombre, self.edad) 

personas =[
    Persona("Juan",15),
    Persona("Andres",25),
    Persona("Xiomara",22),
    Persona("Lizeth",21)
]

menorEdad = filter(lambda Persona: Persona.edad<18, personas)
for menor in menorEdad:
    print(menor)
