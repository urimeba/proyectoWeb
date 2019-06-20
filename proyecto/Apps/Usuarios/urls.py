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
    path('', views_usuarios.login_view),
    path('login', views_usuarios.login_view, name = 'login'),
    path('registrarUsuario', views_usuarios.registrar_usuario, name="registrarUsuario"),
    path('iniciarSesion', views_usuarios.iniciarSesion, name="iniciarSesion"),
    path('cerrarSesion', views_usuarios.cerrarSesion, name="cerrarSesion"),
    path('update', views_usuarios.update_view, name="update"),
    path('obtenerDatosUsuario', views_usuarios.obtenerDatosUsuario, name="obtenerDatosUsuario"),
    path('cambiarDatosUsuario', views_usuarios.cambiarDatosUsuario, name="cambiarDatosUsuario"),
    
    
    
]
