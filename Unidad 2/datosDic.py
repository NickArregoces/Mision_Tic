nombre=input("Por favor ingrese su nombre: ")
edad=input("Por favor ingrese su edad: ")
direccion=input("Por favor ingrese su direccion: ")
telefono=input("Por favor ingrese su telefono: ")

persona={"nombre": nombre, "edad": edad, "direccion": direccion,"telefono":telefono}

print("la persona ",persona["nombre"]," tiene", persona["edad"], " años y su telefono es ", persona["telefono"], " y vive en ", persona["direccion"])