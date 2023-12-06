from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("crear", views.crear_cliente, name="crear-material"),
]
