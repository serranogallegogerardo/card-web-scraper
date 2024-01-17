Attribute VB_Name = "Módulo2"
Sub QuitarMargenes()
    With ActiveDocument.PageSetup
        .LeftMargin = 0
        .RightMargin = 0
        .TopMargin = 0
        .BottomMargin = 0
    End With
End Sub
