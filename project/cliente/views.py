from django.shortcuts import render
from . import models
from .forms import ClienteBuscarFormulario,ClienteFormulario

# Create your views here.
def home(request):
    if request.method == "GET":
        context = ClienteBuscarFormulario()
        clientes = models.Cliente.objects.all()
        return render(request,"cliente/index.html", {'form':context, 'clientes':clientes})
    else:
        form = ClienteBuscarFormulario(request.POST)
        if form.is_valid():
            context = ClienteBuscarFormulario()
            form = form.cleaned_data
            clientes = models.Cliente.objects.filter(nombre__contains=request.POST['nombre'])
            return render(request,"cliente/index.html", {'form':context, 'clientes':clientes})


def crear_cliente(request):
    if request.method == "GET":
        context = {"form":ClienteFormulario()}
        return render(request, "cliente/formulario_crear_cliente.html", context)
    else:
        form = ClienteFormulario(request.POST)
        if form.is_valid():
            form.save()
        context = {"form":ClienteFormulario()}
        return render(request, "cliente/formulario_crear_cliente.html", context)
