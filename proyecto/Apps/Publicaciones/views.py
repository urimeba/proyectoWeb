from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias
from Apps.Categorias import models as models_categorias
from Apps.Publicaciones import models as models_publicaciones
from Apps.Comentarios import models as models_comentarios
import json

# Create your views here.

def obtenerPostsCategorias(request):
    id = request.POST.get('json_name')
    id = int(id)
    publicaciones = []

    if id==0:
        categorias = models_categorias.Categorias.objects.all()
        for categoria in categorias:
            try:
                posts = models_publicaciones.Publicaciones.objects.filter(categoria_id=categoria.id,colonia_id=request.session['colonia']).latest('fecha')
                publicaciones.append(posts)
            except Exception as e:
                print(e)
        return render(request, 'publicaciones.html', {'publicaciones':publicaciones})
    else:
        try:
            posts = models_publicaciones.Publicaciones.objects.filter(categoria_id=id,colonia_id=request.session['colonia'])
        except Exception as e:
            print(e)
    return render(request, 'publicaciones.html', {'publicaciones':posts})



def obtenerPost(request):
    id = request.POST.get('json_name')
    id = int(id)
    
    comments =  []

    post = models_publicaciones.Publicaciones.objects.filter(id=id)

    comentarios = models_comentarios.comentarios_publicaciones.objects.filter(publicacion_id=id)

    for comentario in comentarios:
        comments.append(models_comentarios.Comentarios.objects.filter(id=comentario.id))

    return render(request, 'comentarios.html', {'publicaciones':post,'comentarios':comments})

    