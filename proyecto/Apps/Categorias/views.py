from django.shortcuts import render
from Apps.Categorias import models as models_categorias

# Create your views here.
def obtenerCategorias(request):
    categorias = models_categorias.Categorias.objects.all()

    for categoria in categorias:
        print(categoria)

    return render(request, "base.html", {'categorias':"respuesta"})
