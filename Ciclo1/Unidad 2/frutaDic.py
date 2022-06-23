frutas={"Mango":30.3, "Guanabana": 10.3, "Banano":20.3, "Naranja": 5.5}

fruta=input("¿Cual fruta va a comprar?: ") .title()
kilos=float(input("¿Cuantos kilos desea?: "))

if fruta in frutas:
    print("la fruta ", fruta,kilos, " kilos, tiene un precio de: $", frutas[fruta]*kilos)
else:
    print(f"La fruta {fruta} no esta disponible")