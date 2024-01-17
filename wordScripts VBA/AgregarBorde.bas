Attribute VB_Name = "Módulo4"
Sub AplicarFormatoImagenes()
    ' Aplicar relleno y línea a las imágenes en línea en el documento activo
    
    Dim imagen As InlineShape

    ' Iterar sobre todas las imágenes en línea en el documento
    For Each imagen In ActiveDocument.InlineShapes
        ' Aplicar formato de línea
        With imagen.Line
            .Visible = msoTrue ' Hacer visible la línea
            .ForeColor.RGB = RGB(0, 0, 0) ' Color de la línea (negro en este caso)
            .Weight = 1 ' Ancho de la línea en puntos
        End With

        ' Aplicar formato de relleno
        With imagen.Fill
            .Visible = msoTrue ' Hacer visible el relleno
            .ForeColor.RGB = RGB(255, 0, 0) ' Color del relleno (rojo en este caso)
            .Transparency = 0 ' Transparencia (0 para opacidad completa)
        End With
    Next imagen
End Sub

