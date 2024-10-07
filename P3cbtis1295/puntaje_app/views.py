from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def juguetes(request):
    return render(request, 'juguetes.html')
def marcas(request):
    return render(request, 'marcas.html')
def clientes(request):
    return render(request, 'clientes.html')
def empleados(request):
    return render(request, 'empleados.html')


