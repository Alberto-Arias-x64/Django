from django import forms

class Formulario_de_contacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()