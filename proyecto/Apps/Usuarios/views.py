from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def registrar_usuario(request):
    colonia = request.POST.get('colonia')
    usuario = request.POST.get('usuario')
    contraseña = request.POST.get('contraseña')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    correo = request.POST.get('correo')

    # VERIFICANDO QUE EXISTA UN USUARIO CON ESE CORREO.
    # SI EXISTE, SE VA HACIA EL EXCEPTION
    try:
        usuario_correo = User.objects.get(email=correo)
        return HttpResponse("Error: Ese correo ya esta tomado")
    except Exception as e:
        print(e)

        # INTENTAMOS CREAR EL USUARIO
        try:
            usuario = User.objects.create_user(usuario, correo, contraseña)
            usuario.first_name = nombre
            usuario.las_name = apellido
            usuario.save()
            return HttpResponse("Registro exitoso")
        except Exception as e:
            print(e)
            return HttpResponse("Error: el usuario ya existe")


def iniciarSesion(request):
    usuario = request.POST.get('usuario')
    contraseña = request.POST.get('contraseña')

    user = authenticate(username=usuario, password=contraseña)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Inicio de sesion correcto")
        else:
            return HttpResponse("Error: datos incorrectos")
    else:
        return HttpResponse("Error: datos incorrectos")





    

