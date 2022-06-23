import numpy as np

a1=np.array([1,2,3,4])
print(a1)
print()

a2=np.array([[1,2,3,4], [5,6,7,8]])#array de dos dimensiones
print(a2)
print(a2[1,0])#posiciones en array
print(a2[0,3])
print()

a3= np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]]])
print(a3)
print()

c=np.array([[1,2,3,4], [5,6,7,8]])
b=np.array([[4,7,8,10], [5,6,11,8]])
print(c+b)#Suma de Arrays
print(c-b)#Resta de Arrays
print(c*b)
print(c/b)
print(c**2)
