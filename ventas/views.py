from django.shortcuts import render

# Create your views here.

def PageInicio(request):
    return render(request,"inicio.html")


def PageProductos(request):
    return render(request,"productos.html")
