letra = input(("Digite la letra: ")) .lower() #para transfomar lo que escribe el usuario en minuscula; upper() es para lo contrario

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra es una vocal")
else:
    print("La letra es un consonante")