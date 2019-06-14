from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias
from Apps.Categorias import models as models_categorias
from Apps.Publicaciones import models as models_publicaciones
import json

# Create your views here.

def obtenerPostsCategorias(request,pk):
    idCategoria = pk
    resultado = []
    publicaciones = models_publicaciones.Publicaciones.objects.filter(categoria_id=idCategoria)

    for publicacion in publicaciones:
        resultado.append([publicacion.id, publicacion.titulo, publicacion.descripcion, publicacion.categoria_id, publicacion.fecha])
    return JsonResponse({'publicaciones':resultado})