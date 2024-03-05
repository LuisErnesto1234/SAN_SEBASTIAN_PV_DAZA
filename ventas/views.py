from django.shortcuts import render

# Create your views here.

def PageInicio(request):
    return render(request,"inicio.html")
