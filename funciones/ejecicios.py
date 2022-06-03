#Debes calcular la velocidad
def vel(tiempo:int, distancia:int):
    velocidad = distancia / tiempo
    return "la velocidad es : {} metros/segundos" .format(velocidad)
tiempo = int(input("digite el tiempo(en segundos): "))
distancia = int(input("Digite distancia (en metros): "))
print(vel(tiempo,distancia))


#Debes calcular el area circulo
def circulo (radio: float):
    
    area = (3.1416 * (radio ** 2))
    return "El area del circulo es: {}" .format(area)

radio = float(input("Digite el radio del circulo: "))
print(circulo(radio))



#Debes calcular el perimetro y area de un triangulo
def triangulo (base:float, lado:float, altura:float):
    perimetro = base + lado + altura
    area= (base * altura)/ 2
    return "el perimetro del triangulo es: {} cm y el area es de: {} cm" .format(area,perimetro)

base= float(input("Escriba la base del triangulo: "))
lado= float(input("Escriba el lado del triangulo: "))
altura= float(input("Escriba la altura del triangulo: "))
print(triangulo(base, lado, altura))

#Hallar la distancia
def distancia (velocidad:float, tiempo:float):
    distancia = velocidad*tiempo
    return "La distancia recorrida es {} km/h".format(distancia)

velocidad= float(input("Ingrese la velocidad registrada: (km)"))
tiempo= float(input("Ingrese el tiempo registrado (en segundo): "))

print(distancia(velocidad,tiempo))

#Ecuacion
def ecuacion (num1:float, num2:float):
    x= num2 - num1
    return "La ecuacion es {} + {} = {}" .format (num1,x,num2)

print (ecuacion (10,24))

#calcular promedio del estudiante
def notas(num1:float,num2:float,num3:float):
    promedio= (num1 + num2 + num3)/3
    return "El promedio del estudiante es: {}" .format (promedio)

num1= float(input("escriba la nota 1: "))
num2= float(input("escriba la nota 2: "))
num3= float(input("escriba la nota 3: "))

print (notas(num1,num2,num3))

# Calcular el salario semanal de un trabajador
def nomina (horas:int, salario:int):
    salarioSemanal= horas*salario
    return "El salario semanal del trabajador es: {}" .format (salarioSemanal)

horas= int(input("Escriba las horas trabajadas en la semana: "))
salario=int(input("Escriba su salario por horas: "))

print (nomina(horas,salario))

#
def dinero(guillermo:int):
    luis= guillermo/2
    juan= (guillermo+luis)/2
    total= luis +guillermo +juan
    return "El dinero que tiene Luis es: {}, el que tiene Juan es: {} y el total de los tres es: {}" .format(luis, juan,total)

guillermo= int(input("Escriba el dinero que tiene Guillermo: "))

print (dinero(guillermo))
    
