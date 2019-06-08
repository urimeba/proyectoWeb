from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias
from Apps.Categorias import models as models_categorias
import json

# Create your views here.
def index(request):
    categorias = models_categorias.Categorias.objects.all()
    respuesta = []

    for categoria in categorias:
        respuesta.append(categoria.nombre)



    
    return render(request, "base.html", {'categorias':respuesta})
