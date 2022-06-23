def notas(informacion:dict):
    nota= informacion["nota"]
    
    if nota >= 0 and nota <=5:
        return ("Su nota es insuficiente")
    elif nota >=6 and nota <=7:
        return ("Su nota es suficiente")
    elif nota >=8 and nota <=9:
        return ("Su nota es buena")
    elif nota >9 and nota <=10:
        return ("Su nota es excelente")
    else:
        return("Nota no valida")

nota=float(input("Digita la nota de 0 a 10: "))

informacion={"nota":nota}
print(notas(informacion))