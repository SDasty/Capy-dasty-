from django import forms

class CalculadoraNotasForm(forms.Form):
    
    asignatura = forms.CharField(max_length=100)
    nota = forms.DecimalField(max_digits=5, decimal_places=2)
    creditos = forms.IntegerField()
