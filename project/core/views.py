from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"core/index.html")

def contacto(request):
    return render(request, 'core/contacto_page.html')
