from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def clientes(request):
    return render(request,"clientes.html")

def productos(request):
    return render(request,"productos.html")

def proveedores(request):
    return render(request,"proveedores.html")

def inventario(request):
    return render(request,"inventario.html")