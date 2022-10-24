SELECT Constructora, Banco_Vinculado, Clasificacion, Ciudad , Numero_Habitaciones FROM Proyecto
 WHERE Numero_Habitaciones not BETWEEN 2 and 4
 ORDER by Numero_Habitaciones