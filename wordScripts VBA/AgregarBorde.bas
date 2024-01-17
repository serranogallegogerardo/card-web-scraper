Attribute VB_Name = "M�dulo4"
Sub AplicarFormatoImagenes()
    ' Aplicar relleno y l�nea a las im�genes en l�nea en el documento activo
    
    Dim imagen As InlineShape

    ' Iterar sobre todas las im�genes en l�nea en el documento
    For Each imagen In ActiveDocument.InlineShapes
        ' Aplicar formato de l�nea
        With imagen.Line
            .Visible = msoTrue ' Hacer visible la l�nea
            .ForeColor.RGB = RGB(0, 0, 0) ' Color de la l�nea (negro en este caso)
            .Weight = 1 ' Ancho de la l�nea en puntos
        End With

        ' Aplicar formato de relleno
        With imagen.Fill
            .Visible = msoTrue ' Hacer visible el relleno
            .ForeColor.RGB = RGB(255, 0, 0) ' Color del relleno (rojo en este caso)
            .Transparency = 0 ' Transparencia (0 para opacidad completa)
        End With
    Next imagen
End Sub

