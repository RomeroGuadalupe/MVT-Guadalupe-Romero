from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from GrupoFamiliar.models import familia
# Create your views here.

def familiares (request):
    
    familiar = familia.objects.all()

    lista_integrantes = []
    
    for integrante in familiar:
        info = f"Mi {integrante.parentesco} se llama {integrante.nombre} {integrante.apellido}, tiene {integrante.edad} años y nacio el {integrante.fecha_nacimiento}"

        lista_integrantes.append(info) 
       
    datos = {"familiares":lista_integrantes}

    archivo = open(r"C:\Users\Guadalupe\Desktop\CODER\PYTHON\ENTREGA FAMILIA\familia\MiFamilia\GrupoFamiliar\Template\index.html","r")
    contenido_html = archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)
    contexto = Context(datos)

    doc_a_renderizar = plantilla.render (contexto)
    return HttpResponse(doc_a_renderizar)






