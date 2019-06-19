from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias
from Apps.Categorias import views as views_categorias
import json
from Apps.Usuarios import forms

# Create your views here.
def login_view(request):     
    if 'colonia' in request.session:
        return redirect(views_categorias.obtenerCategorias)
    else:
        return render(request,'login.html')

def registrar_usuario(request):
    datos = request.POST.get('json_name')
    datos = json.loads(datos)
    colonia = datos['colonia']
    usuario = datos['usuario']
    contraseña = datos['contraseña']
    nombre = datos['nombre']
    apellido = datos['apellido']
    correo = datos['correo']

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
            id_colonia = models_colonias.Colonias.objects.get(nombre=colonia).id
            id_usuario = usuario.id
            
            # AGREGANDO EL USUARIO A USUARIOS_USUARIOS
            usuario_usuario = models_usuarios.Usuarios(colonia_id=id_colonia, usuario_id=id_usuario)
            usuario_usuario.save()
            return HttpResponse("Registro exitoso")
        except Exception as e:
            print(e)
            return HttpResponse("Error: el usuario ya existe")


def iniciarSesion(request):
    datos = request.POST.get('json_name')
    datos = json.loads(datos)
    usuario = datos['usuario']
    password = datos['contraseña']
    user = authenticate(username=usuario, password=password)
    respuesta = ""

    if user is not None:
        if user.is_active:
            login(request, user)
            colonia = models_usuarios.Usuarios.objects.get(id=user.id).colonia_id
            request.session['colonia'] = colonia
            request.session['nombreColonia'] = models_colonias.Colonias.objects.get(id=colonia).nombre
            print("Inicio de sesion correcto")
            respuesta = True
        else: 
            print("Datos incorrectos 1")
            respuesta = False
    else:
        print("Datos incorrectos 2")
        respuesta = False
    return HttpResponse(respuesta)

def cerrarSesion(request):
    del request.session['colonia']
    request.session.flush()
    return redirect('/')

def update_view(request):
    if request.method == 'POST':
        form = forms.ActualizarDatos(request.POST)
        
        if form.is_valid():
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            correo = request.POST.get('correo')
            contraseña = request.POST.get('contraseña')
            colonia = request.POST.get('colonia')

            print(nombre)

        else:
            print("El formulario esta mal")
            return redirect('update_view')
    else:
        form = forms.ActualizarDatos()
        return render(request, "update.html", {'form':form})