from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from Apps.Colonias import models as models_colonias

# Create your views here.
def obtenerColonias(request):
    colonias = models_colonias.Colonias.objects.all()
    respuesta = []

    for colonia in colonias:
        respuesta.append(colonia.nombre)

    return JsonResponse({respuesta})

