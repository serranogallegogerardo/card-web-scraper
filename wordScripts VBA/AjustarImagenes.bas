Attribute VB_Name = "M�dulo1"
Sub ajustar_imagenes()
    Dim Alto As Single
    Dim Ancho As Single
    
    ' Definir las dimensiones deseadas en mil�metros
    Alto = CentimetersToPoints(8.9)  ' 89 mil�metros
    Ancho = CentimetersToPoints(6.3) ' 63 mil�metros

    For Each imagen In ActiveDocument.InlineShapes
        ' Ajustar el alto y el ancho de la imagen
        imagen.LockAspectRatio = msoFalse ' Desbloquear la proporci�n
        imagen.Height = Alto
        imagen.Width = Ancho
    Next
End Sub

