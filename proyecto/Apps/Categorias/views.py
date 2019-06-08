from django.shortcuts import render
from Apps.Categorias import models as models_categorias

# Create your views here.
def obtenerCategorias(request):
    categorias = models_categorias.Categorias.objects.all()
    respuesta = []

    for categoria in categorias:
        respuesta.append(categoria.nombre)

    print(respuesta)
    return render(request, "base.html", {'categorias':respuesta})
