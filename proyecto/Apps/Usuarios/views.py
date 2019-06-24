from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
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

    try:

        user = authenticate(username=usuario, password=password)
        respuesta = ""

        if user is not None:
            if user.is_active:
                login(request, user)
                colonia = models_usuarios.Usuarios.objects.get(id=user.id).colonia_id
                request.session['colonia'] = colonia
                request.session['nombreColonia'] = models_colonias.Colonias.objects.get(id=colonia).nombre.upper()
                print("Inicio de sesion correcto")
                respuesta = True
            else: 
                print("Datos incorrectos 1")
                respuesta = False
        else:
            print("Datos incorrectos 2")
            respuesta = False
        return HttpResponse(respuesta)
    except Exception as e:
        print(e)
        return HttpResponse(False)

def cerrarSesion(request):
    del request.session['colonia']
    request.session.flush()
    return redirect('/')

def update_view(request):
    if 'colonia' in request.session:

        if request.method == 'POST':
            form = forms.ActualizarDatos(request.POST)
            
            if form.is_valid():
                nombre = request.POST.get('nombre')
                apellido = request.POST.get('apellido')
                correo = request.POST.get('correo')
                contraseña = request.POST.get('contraseña')
                contraseña2 = request.POST.get('contraseña2')
                colonia = request.POST.get('colonia')
                if contraseña == "" and contraseña2=="":
                    usuario = User.objects.get(username=request.user)
                    usuario.first_name=nombre
                    usuario.last_name=apellido
                    usuario.email=correo
                    usuario.save()

                    user = models_usuarios.Usuarios.objects.get(usuario_id=usuario.id)
                    user.colonia_id=colonia
                    user.save()

                    request.session['colonia'] = colonia
                    request.session['nombreColonia'] = models_colonias.Colonias.objects.get(id=colonia).nombre.upper()
                    messages.add_message(request, messages.INFO, "Datos actualizados correctamente")
                    return redirect('update')
                elif contraseña == contraseña2:
                    usuario = User.objects.get(username=request.user.username)
                    usuario.first_name=nombre
                    usuario.last_name=apellido
                    usuario.email=correo
                    usuario.set_password(contraseña)
                    usuario.save()

                    login(request, usuario)
                    request.session['colonia'] = colonia
                    request.session['nombreColonia'] = models_colonias.Colonias.objects.get(id=colonia).nombre.upper()

                    user = models_usuarios.Usuarios.objects.get(usuario_id=usuario.id)
                    user.colonia_id=colonia
                    user.save()

                    messages.add_message(request, messages.INFO, "Datos y contraseña actualizados correctamente")

                    return redirect('update')
                else:
                    messages.add_message(request, messages.INFO, "Las contraseñas no coinciden. Favor de verificar")
                return redirect('update')
            else:
                print("El formulario esta mal")
                return redirect('update')
        else:
            form = forms.ActualizarDatos()
            colonia = models_usuarios.Usuarios.objects.get(id=request.user.id).colonia.id
            form.fields['colonia'].initial = [colonia]
            return render(request, "update.html", {'form':form})
    else:
        return redirect('login')
    
def obtenerDatosUsuario(request):
    usuario = models_usuarios.Usuarios.objects.get(usuario_id=request.user.id)

    nombre=usuario.usuario.first_name
    apellido = usuario.usuario.last_name
    correo = usuario.usuario.email
    colonia = usuario.colonia.nombre

    datos={}
    datos['nombre'] = nombre
    datos['apellido'] = apellido
    datos['correo'] = correo
    datos['colonia'] = colonia
    return JsonResponse({'datos':datos})

def cambiarDatosUsuario(request):
    return HttpResponse("Hola")

