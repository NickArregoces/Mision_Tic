DicMeses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
                                # 0  1  2
fecha=input("Introduzca la fecha en formato dd/mm/aaaa: ")
fecha =fecha.split("/")#separa cada elemento que escriba el usuario con /

print(fecha[0]," del mes ", DicMeses[int(fecha[1])], " del año ", fecha[2])
