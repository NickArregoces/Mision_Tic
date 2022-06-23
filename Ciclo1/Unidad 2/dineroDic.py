monedas= {"Euro": "€", "Dollar":"$", "Yen": "¥"}

divisa= input("Ingrese la divisa: ")

if divisa.title() in monedas: # busca en el diccionario lo escrito por el usuario
    print(monedas[divisa.title()])# .title convierte en mayuscula o minuscula
else:
    print("Lo sentimos, no se encuentra la divisa")