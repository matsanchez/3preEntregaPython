from django.shortcuts import render
from . import models
from .forms import ProductoFormulario, ProductoBuscarFormulario

# Create your views here.
def home(request):
    if request.method == "GET":
        context = ProductoBuscarFormulario()
        productos = models.Producto.objects.all()
        return render(request,"producto/index.html", {'form':context, 'productos':productos})
    else:
        form = ProductoBuscarFormulario(request.POST)
        if form.is_valid():
            context = ProductoBuscarFormulario()
            form = form.cleaned_data
            productos = models.Producto.objects.filter(nombre__contains=request.POST['nombre'])
            return render(request,"producto/index.html", {'form':context, 'productos':productos})


def crear_producto(request):
    if request.method == "GET":
        #mostrar formulario
        context = {"form":ProductoFormulario()}
        return render(request, "producto/formulario_crear_producto.html", context)
    else:
        form = ProductoFormulario(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return render(request,"producto/index.html")
