'''Una entidad Bancaria o entidad financiera, requiere calcular el valor de los intereses ganados y el total final de dinero para diferentes clientes, de acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira antes de este periodo se aplica una penalidad del 2%.'''

def CDT(usuario:str,capital:int, tiempo:int):
    if tiempo <=2:
        valorTotal= capital-(capital* 0.02)
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format(usuario,str(capital),str(tiempo),str(valorTotal))
    else:
        valorIntereses= (capital*0.03*tiempo)/12
        valorTotal=valorIntereses+capital
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format(usuario,str(capital),str(tiempo),str(valorTotal))
    
#print(CDT("AB1012", 1000000, 3))
#print(CDT("QW3456",5000000,2))
    

# Si se desea que el usuario ingrese los datos:
# usuario= str(input("por favor escriba su usuario: "))
# capital= int(input("por favor escriba el monto a ingresar: "))
# tiempo= int(input("por favor escriba el tiempo del CDT: "))
