def AutoPartes(ventas:list):
    venta={}
    for idProducto, dProducto, pnProducto, cvProducto, sProdcuto, nComprador, cComprador, fVenta in ventas:
        if venta.get(idProducto) == None:#.get Busca en el dicc la clave, si el valor es nulo entonces:
            venta[idProducto] =[]
        venta[idProducto].append((dProducto, pnProducto, cvProducto, sProdcuto, nComprador, cComprador, fVenta))          
    return venta

def consultaRegistro(ventas,idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProdcuto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print("Producto consultado: " ,idProducto, " Descripción ", dProducto, " #Parte ", pnProducto, " Cantidad vendida ", cvProducto," Stock ", sProdcuto, " Comprador", nComprador," Documento ", cComprador, " Fecha Venta ", fVenta)
        
    else:
        print ("No hay registro de venta de ese producto")


consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()
consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujia', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujia', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()


