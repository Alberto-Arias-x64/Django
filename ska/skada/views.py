from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
def saludo(request):
    fecha_actual=datetime.datetime.now()
    nombre="Simio"
    diccionario={"nombre_persona":nombre,"lista":["kk1","kk2","kk3","kk4"],"fecha":fecha_actual}
    #doc_externo=open("C:/Users/nikol/Documents/django/skada/skada/plantillas/plantilla1.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #ctx=Context({"nombre_persona":nombre,"lista":["kk1","kk2","kk3","kk4"],"fecha":fecha_actual})
    #documento=plt.render(ctx)
    #///////////////////////////////////////////////////////////////////////#
    #documeto_x=loader.get_template('plantilla1.html')
    #ctx={"nombre_persona":nombre,"lista":["kk1","kk2","kk3","kk4"],"fecha":fecha_actual}
    #documento=documeto_x.render(ctx)
    #return HttpResponse(documento)
    #////////////////////////////////////////////////////////////////////////#
    return render(request,"plantilla1.html",diccionario)

def despedida(request):
    return HttpResponse("Adios sin kk")

def fecha(request):
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora sin kk %s
    </h1>
    </body>
    </html>""" %fecha_actual.day

    return HttpResponse(documento)

def calculadora(request,edad,anno):
    
    edad_actual=edad
    periodo=anno-2020
    edad_futura=edad_actual+periodo

    documento="""<html>
    <body>
    <h2>
    En el año %s tendras %s años 
    </h2>
    </body>
    </html>""" %(anno, edad_futura)

    return HttpResponse(documento)

def heredar(request):
    return render(request, "plantilla_heredada.html")