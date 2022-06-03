def dinero(nAutosVendidos: int, precioAuto: float) -> str:
        
    salarioMes = 800000
        
    salarioFinal = salarioMes + (nAutosVendidos * 150000) + (0.05 *precioAuto*nAutosVendidos)

    return "El salario de este mes para el vendedor es de : {}$".format(salarioFinal)

print(dinero(5,5000000)) 