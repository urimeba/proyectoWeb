from django.shortcuts import render, redirect, HttpResponse
from Apps.Categorias import models as models_categorias
from Apps.Publicaciones import models as models_publicaciones
from Apps.Colonias import models as models_colonias
from django.db.models import Count
from django.contrib.auth.models import User
from Apps.Publicaciones import forms

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

        if request.method=='POST':
            form = forms.PublicacionFormulario(request.POST)
            if form.is_valid():
                titulo = request.POST.get('titulo')
                descripcion = request.POST.get('descripcion')
                categoria = request.POST.get('categoria')
                models_publicaciones.Publicaciones.create(titulo=titulo,descripcion=descripcion,categoria_id=categoria,colonia_id=request.session['colonia'],usuario_id=request.user.id)
            else:
                print("EL FORMULARIO ESTA MAL")
            return redirect('obtenerCategorias')
        else:
            form = forms.PublicacionFormulario()
            return render(request, "base.html", {'categorias':categorias,'publicaciones':publicaciones,'form':form})
    else:
        return redirect('/')


    

    
