def cliente(informacion:dict)->dict:
    pass
    parque={'nombre':'','edad':0,"atraccion":'','apto':False,'primer_ingreso':False,'total_boleta':0}
    
    parque['edad']=informacion['edad']
    parque['nombre']=informacion['nombre']
    parque['primer_ingreso']=informacion['primer_ingreso']
    parque['apto']=True
    
    if parque['edad']>18:
        parque['atraccion']='X-Treme'
        parque['total_boleta']=20000
        parque['apto']=True
        if parque['primer_ingreso']==True:
            parque['total_boleta']= parque['total_boleta']- parque['total_boleta']*0.05
        else:
            parque['total_boleta']=20000 
    elif parque['edad'] >=15 and parque['edad']<=18: 
        parque['atraccion']='Carros chocones'
        parque['total_boleta']=5000
        parque['apto']=True
        if parque['primer_ingreso']==True:
            parque['total_boleta']= parque['total_boleta']- parque['total_boleta']*0.07
        else:
            parque['total_boleta']=5000
    elif parque['edad'] >=7 and parque['edad']<15: 
        parque['atraccion']='Sillas voladoras'
        parque['total_boleta']=10000
        parque['apto']=True
        if parque['primer_ingreso']==True:
            parque['total_boleta']= parque['total_boleta']- parque['total_boleta']*0.05
        else:
            parque['total_boleta']=10000
    else:
        parque['atraccion']='N/A'
        parque['apto']=False
        parque['total_boleta']='N/A'
    return parque
           
diccionario={'id_cliente':4,'nombre': 'Johana Fernandez', 'edad': 8,'primer_ingreso': False}

diccionario1=cliente(diccionario)
print(diccionario1) 

