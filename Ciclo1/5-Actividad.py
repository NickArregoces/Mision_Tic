def triangulo(base: float, lado: float, altura:float ) -> str:
        
    perimetro = base + lado + lado
    
    area = (base * altura)/2
     
    return  "El perimetro del triangulo es de  {}cm y el area es de {}cm ".format(perimetro,area)

print(triangulo(20,80.29,84))
print(triangulo(10,43.17,42))
 