Attribute VB_Name = "Módulo1"
Private Sub IncreaseSharpnessSesCinco()
    Dim Pic As InlineShape

    For Each Pic In ActiveDocument.InlineShapes
        With Pic.Fill.PictureEffects
            Dim eff As PictureEffect
            Set eff = .Insert(msoEffectSharpenSoften)
            eff.EffectParameters(1).Value = 0.65
        End With
    Next
End Sub
