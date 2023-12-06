from django import forms
from .models import Producto, Categoria



class ProductoFormulario(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['imagen','nombre', 'categoria', 'precio','descripcion', 'stock', 'vendidos']
        labels = {'imagen':'Subir Foto','nombre': 'Nombre', 'categoria': 'Categoria', 'precio': 'Precio','descripcion': 'Descripcion', 'stock': "Stock", 'vendidos': 'Vendidos'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'stock': forms.TextInput(attrs={'class':'form-control'}),
            'vendidos': forms.TextInput(attrs={'class':'form-control'})
        }

class ProductoBuscarFormulario(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre']
        labels = {'nombre':''}
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Buscar...'})}
