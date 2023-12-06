from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path("", views.home, name="index"),
    path('crear', views.crear_producto, name="crear-producto")
]
