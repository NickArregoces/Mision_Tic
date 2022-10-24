SELECT Constructora, Banco_Vinculado, Clasificacion, Ciudad , Numero_Habitaciones FROM Proyecto
 WHERE Ciudad like "m%" /*"%e"  || not like*/
 ORDER by Ciudad