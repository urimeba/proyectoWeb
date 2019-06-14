from django.shortcuts import render, redirect, HttpResponse
from Apps.Categorias import models as models_categorias
from Apps.Publicaciones import models as models_publicaciones
from Apps.Colonias import models as models_colonias
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.
def obtenerCategorias(request):
    if 'colonia' in request.session:
        publicaciones = []
        categorias = models_categorias.Categorias.objects.all()

        for categoria in categorias:
            try:
                posts = models_publicaciones.Publicaciones.objects.filter(categoria_id=categoria.id).latest('fecha')
                publicaciones.append(posts)
            except Exception as e:
                print(e)

        return render(request, "base.html", {'categorias':categorias,'publicaciones':publicaciones})
    else:
        return redirect('/')


    

    
