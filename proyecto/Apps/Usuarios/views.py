from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias

# Create your views here.

def registrar_usuario(request):
    colonia = request.POST.get('colonia')
    usuario = request.POST.get('usuario')
    contraseña = request.POST.get('contraseña')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    correo = request.POST.get('correo')

    # VERIFICANDO QUE EXISTA UN USUARIO CON ESE CORREO.
    # SI NO EXISTE, SE VA HACIA EL EXCEPTION
    try:
        usuario_correo = User.objects.get(email=correo)
        return HttpResponse("Error: Ese correo ya esta tomado")
    except Exception as e:
        print(e)

        # INTENTAMOS CREAR EL USUARIO
        try:
            # AGREGANDO EL USUARIO A USER.AUTH
            usuario = User.objects.create_user(usuario, correo, contraseña)
            usuario.first_name = nombre
            usuario.last_name = apellido
            usuario.save()

            # OBTENEMOS EL ID DE LA COLONIA ELEGIDA Y EL ID DEL USUARIO CREADO AQUI ARRIBA
            id_colonia = models_colonias.Colonias.get(nombre=colonia).id
            id_usuario = usuario.id
            
            # AGREGANDO EL USUARIO A USUARIOS_USUARIOS
            usuario_usuario = models_usuarios.Usuarios(colonia_id=id_colonia, usuario_id=id_usuario)
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

            id_colonia = models_usuarios.Usuarios.get(id=user.id).colonia_id
            request.session['colonia'] = id_colonia

            return HttpResponse("Inicio de sesion correcto")
        else:
            return HttpResponse("Error: datos incorrectos")
    else:
        return HttpResponse("Error: datos incorrectos")

def cerrarSesion(request):
    del request.session['colonia']
    return redirect('/')

def login_view(request):     
    return render(request,'login.html')