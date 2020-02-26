#*
# Codigo Ronald:
# Notas:
#   - Para hacer una peticion y enviar una respuesta Django trabaja con 2 clases fundamentales:
#       -Request: para hacer una peticion.
#       -HttpResponse: para enviar la informacion o la respuesta.
#   - Cuando una pagina es requerida REQUESTED, Django crea un objeto HttpRequest que contiene los metadados acerca de la petición.
#   -Una vista se crea simplemente declarando una funcion Python
#   - Todo en una URL, por defecto, es considerado texto. 
# Archivos creados:
#   -views.py: corresponde a las vistas que vayamos almacenando. Por convención se suele llamar con este nombre.
# 
# *#

from django.http import HttpResponse   
import datetime
from django.template import  Template, Context


def saludo(request):
    documento="""<html>
    <body>
    <h2>
    Hola alumnos de Prácticas intermedias
    </h2>
    </body>
    </html>"""

    #esto es dificil de esta forma, mis compañeros hablarán de una forma mas sencilla de hacerlo
    doc_externo=open('C:/Users/ronald/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    plt=Template(doc_externo.read())
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Prácticas intermedias")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    #edadActual=18
    periodo=agno-2020
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h2>
    En el año  %s tendras %s años
    </h2>
    </body>
    </html>""" %(agno, edadFutura)
    return HttpResponse(documento)

