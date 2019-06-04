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
from Apps.Usuarios import views as views_usuarios

urlpatterns = [
    # LAS VIEWS SE ENCUENTRAN COMENTADAS
    # SI LAS OCUPAS, DESCOMENTALAS
    # path('Categorias', include('Apps.Categorias.urls')),
    path('registrarUsuario', views_usuarios.registrar_usuario, name="registrarUsuario"),
    path('iniciarSesion', views_usuarios.iniciarSesion, name="iniciarSesion"),


]
