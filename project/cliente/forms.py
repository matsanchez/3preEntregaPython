from django import forms
from .models import Cliente, Pais, Idioma


class ClienteFormulario(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email','nacimiento', 'pais_origen', 'idioma']
        labels = {'nombre': 'Nombre', 'apellido': 'Apellido', 'email': 'Email','nacimiento': 'Nacimiento', 'pais': "Pais", 'idioma': 'Idioma'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'pais_origen': forms.Select(attrs={'class':'form-control'}),
            'idioma': forms.Select(attrs={'class':'form-control'})
        }


class ClienteBuscarFormulario(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre']
        labels = {'nombre':''}
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Buscar...'})}
