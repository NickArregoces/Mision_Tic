a= {1,2,3}
b={3,4,5}
print(a==b)

c= a | b#une los conjuntos
print(c)

c = a & b #los elemento comunes o iguales de conjuntos
print(c) #interseccion de conjuntos

c= a -b
print(c) #quedan los numeros no comunes de a

c= b-a
print(c) #quedan los numeros no comunes de b

c= b ^ a
print(c)#Diferencia simetrica

