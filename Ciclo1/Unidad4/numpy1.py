import numpy as np

a= np.arange(10,50)# es un funcion para rangos
print(a)
print (a[-1])#navegacion inversa
print()
print (a[::-1])#imprime alreves

print()
print(np.arange(0,9).reshape(3,3)) #una matriz de 3 filas y de 3 columna

print()
print(np.arange(0,16).reshape(4,4))

print()
print(np.arange(0,12).reshape(4,3))

print()# impresion ordenada de la lista y sin repetir los valores de la lista,
b= np.array([1,2,3,1,0,0,2,1,3,4,6,3,1,0])
print(np.argwhere(b!=0))

print()
b=np.random.random((3,3))
print(b)

print(b.argmax())
print()
print(b.ravel()[b.argmax()])
print()
print(np.unravel_index(b.argmax(), b.shape))
print(b[np.unravel_index(b.argmax(),b.shape)])

r=np.identity(6)#Matriz de indentidad 6x6
print(r)

#Crear una matriz  con valores al azar con forma 3x3x3
s=np.random.random((3,3,3))
print(s)
print()

print(s.argmin()) #la posicion el numero minimo
print(s.ravel()[s.argmin()])#valor del numero minimo
print()
z=np.ones((10,10))#Matriz 10x10 con 1 en los bordes
z[1:-1,1:-1]=0
print(z)
print()
print(np.tile(np.arange(0,5), 5).reshape(5,5))#Matriz de 5x5 en cada renglon de 0 a 4

a=np.random.random((4,3))
b=np.random.random((4,3))
print(a==b)

