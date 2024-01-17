Attribute VB_Name = "Módulo1"
Sub ajustar_imagenes()
    Dim Alto As Single
    Dim Ancho As Single
    
    ' Definir las dimensiones deseadas en milímetros
    Alto = CentimetersToPoints(8.9)  ' 89 milímetros
    Ancho = CentimetersToPoints(6.3) ' 63 milímetros

    For Each imagen In ActiveDocument.InlineShapes
        ' Ajustar el alto y el ancho de la imagen
        imagen.LockAspectRatio = msoFalse ' Desbloquear la proporción
        imagen.Height = Alto
        imagen.Width = Ancho
    Next
End Sub

