from datetime import datetime
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.template import Template,Context

class Pepo(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
def saludo(request):
    return HttpResponse("Hola ficha 2237520 Tgo ADSISISISI , Esta es la primera pagina con Django")

def despedida(request):
    return HttpResponse("CHAO ES QUE LE DIGO, ATA LA PROXIMAAA")


def texto_en_html(request):
    fecha = datetime.now()
    # nombre = "PEPITO"
    # apellido = "RAMBO"
    persona = Pepo("Nicolas","Ramirez")
    tema_estudiar = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    doc_externo = open(("C:/Users/SENA/Desktop/Todo lo que habia en el escritorio esta aqui/Ficha 2237520/4 trimestre/Lunes_jueves_viernes/Construir_Sistema/Framework, Django/CODIGO/Proyecto1/template/miplantilla.html"))
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"Nombre_persona":persona.nombre,"Apellido_persona":persona.apellido,"Fecha":fecha, "temas":tema_estudiar})

    documento = plt.render(ctx)

    
    return HttpResponse(documento)


def calcularEdad(request,anio):
    edad_actual = 32
    periodo = anio - 2021
    edad_futura = edad_actual + periodo
    documento = "En el año %s tendras %s años "%(anio,edad_futura)
    return HttpResponse(documento)
