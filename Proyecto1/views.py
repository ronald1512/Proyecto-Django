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
from django.template import loader

class Perro(object):
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

def taller (request): 
    
    
    lista = ["uno", "dos", "tres", "cuatro", "cinco"]
    tiempo = datetime.datetime.now()
    #perro1 = Perro("Chispa", "Chihuhua", "10")
    perro2 = Perro("Flash", "DALMATA", "5")
    var_titulo = "Titulo Taller"
    #pagina = open("D:/Universidad/PRACTICAS_INTER/DJANGO/Taller_Checha/Taller_Checha/plantillas/plantilla.html")
    #plt = Template(pagina.read())
    #pagina.close()
    #ctx = Context()
    pagina = loader.get_template("plantilla.html")
    documento = pagina.render({"titulo": var_titulo, "objeto_perro": perro2, "tiempo_actual": tiempo, "numeros": lista})

    return HttpResponse(documento)

def saludo(request):
    documento="""<html>
    <body>
    <h2>
    Hola alumnos de Prácticas intermedias
    </h2>
    </body>
    </html>"""

    #esto es dificil de esta forma, mis compañeros hablarán de una forma mas sencilla de hacerlo
    doc_externo=open('D:/Universidad/PRACTICAS_INTER/Proyecto-Django/Proyecto1/plantillas/miplantilla.html')
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

