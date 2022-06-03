tipo=int(input("Elija el tipo de dulce que desea comprar: 1,2 o 3: "))
can=int(input("Digite la cantidad que desea: "))
dulces={"can":can,"tipo":tipo,"precio":0,"monto":0}

if dulces["tipo"]==1:
    dulces["precio"]=3
    dulces["monto"]= dulces["precio"]*dulces["can"]
    if dulces["can"] <=5:
        dulces["monto"] -= 0.05
    elif dulces["can"] <=10:
        dulces["monto"] = dulces["monto"]-(dulces["monto"]*0.07)
        
elif dulces["tipo"]==2:
    dulces["precio"]=4
    dulces["monto"]= dulces["precio"]*dulces["can"]
    if dulces["can"] >7:
        dulces["monto"] = dulces["monto"]-(dulces["monto"]*0.05)

elif dulces["tipo"]==3:
    dulces["precio"]=5
    dulces["monto"]= dulces["precio"]*dulces["can"]
    if dulces["can"] >4:
        dulces["monto"] = dulces["monto"]-(dulces["monto"]*0.15)
else:
    print("Tipo de dulce no disponible")

print("El tipo de dulce es",dulces["tipo"],"tiene un precio unitario de", dulces["precio"],",el numero de dulces comprados es", dulces["can"], "y tiene un total de", dulces["monto"])
