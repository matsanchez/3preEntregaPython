from django.db import models


class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    imagen=models.ImageField(null=True, blank=True)
    nombre=models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    stock=models.CharField(max_length=100)
    vendidos=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
