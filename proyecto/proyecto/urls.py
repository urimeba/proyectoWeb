"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Apps.Usuarios.urls')),

    # LAS APLICACIONES SE ENCUENTRAN COMENTADAS
    # SI LAS OCUPAS, DESCOMENTALAS
    # path('Categorias', include('Apps.Categorias.urls')),
    # path('Comentarios', include('Apps.Comentarios.urls')),
    # path('Publicaciones', include('Apps.Publicaciones.urls')),
    # path('Usuarios', include('Apps.Usuarios.urls')),
    # path('Colonias', include('Apps.Colonias.urls')),

]
