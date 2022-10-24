SELECT Constructora, Banco_Vinculado, Proyecto.Clasificacion, Ciudad,  Nombre|| " " || Primer_Apellido as "Lider Encargado"
FROM Proyecto INNER JOIN Lider 
on Proyecto.ID_Lider = Lider.ID_Lider
INNER JOIN Tipo
on Proyecto.ID_Tipo = tipo.ID_Tipo
WHERE Ciudad in ("Ibague", "Neiva")
ORDER by Estrato