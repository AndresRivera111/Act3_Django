from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('marcas/', views.marcas, name='marcas'),
    path('clientes/', views.clientes, name='clientes'),
    path('empleados/', views.empleados, name='empleados'),
]