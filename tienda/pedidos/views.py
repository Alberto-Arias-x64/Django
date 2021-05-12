from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from pedidos.forms import Formulario_de_contacto

# Create your views here.

def busqueda_productos(request):
    return render(request,"formulario.html")

def buscar(request):
    if request.GET["product"]:
        #mensaje="articulo buscado: %r" %request.GET["product"]
        producto=request.GET["product"]
        if len(producto)>20:
            mensaje="busqueda demanda muchos recursos"
        else:
            art=articulos.objects.filter(nombre__icontains=producto)
            return render(request,"resultados_busqueda.html",{"art":art,"query":producto})
    else:
        mensaje="No has puesto nada pelotudo"
    return HttpResponse(mensaje)
'''
def contacto(request):
    if request.method=="POST":
        asunto=request.POST["asunto"]
        mensaje=request.POST["mensaje"]+" "+ request.POST["email"]

        email_from=settings.EMAIL_HOST_USER
        recipiente=["nikolas64.98@hotmail.es"]

        send_mail(asunto,mensaje,email_from,recipiente)

        return render(request,"gracias.html")
    return render(request,"contacto.html")
'''

def contacto(request):
    if request.method=="POST":
        miformulario=Formulario_de_contacto(request.POST)
        if miformulario.is_valid():
            inform=miformulario.cleaned_data
            send_mail(inform['asunto'],inform['mensaje'],
            inform.get('email',''),['yugipoi@gmail.com'],)
            return render(request,"gracias.html")
    else:
        miformulario=Formulario_de_contacto()
    return render(request,"formulario_contacto.html",{"form":miformulario})
