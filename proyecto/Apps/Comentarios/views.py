from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from Apps.Comentarios import models as models_comentarios
from Apps.Usuarios import models as models_usuarios

# Create your views here.
def publicarComentario(request):
    datos = request.POST.get('json_name')
    datos = json.loads(datos)

    respuesta = {}

    contenido = datos['comentario']
    publicacion= int(datos['id'])
    usuario = request.user.id
    usuario_usuario = models_usuarios.Usuarios.objects.get(usuario_id=usuario)

    try:
        comentario = models_comentarios.Comentarios(contenido=contenido, usuario=usuario_usuario)
        comentario.save()

        comentario_comentario = models_comentarios.comentarios_publicaciones(comentario_id=comentario.id, publicacion_id=publicacion)
        comentario_comentario.save()
        respuesta['id']=comentario_comentario.comentario.id
        respuesta['contenido']=comentario_comentario.comentario.contenido
        respuesta['fecha']=comentario_comentario.comentario.fecha
        respuesta['usuario']=comentario_comentario.comentario.usuario.usuario.username
    except Exception as e:
        print(e)
  
    return JsonResponse({'respuesta':respuesta})

def eliminarComentario(request):
    idComentario = request.POST.get('json_name')
    idComentario = int(idComentario)

    respuesta = ""

    try:
        comentario = models_comentarios.Comentarios.objects.get(id=idComentario)
        comentario.delete()
        respuesta = True
    except Exception as e:
        print(e)
        respuesta = False

    return HttpResponse(respuesta)

def cambiarComentario(request):
    datos = request.POST.get('json_name')
    datos = json.loads(datos)
    idComentario = datos['idComentario']
    idComentario = int(idComentario)
    comentario = datos['comentario']
    respuesta =""

    try:
        comentario_nuevo = models_comentarios.Comentarios.objects.get(id=idComentario)
        comentario_nuevo.contenido=comentario
        comentario_nuevo.save()
        respuesta="Comentario cambiado"
    except Exception as e:
        print(e)
        respuesta = "Error: intentalo nuevamente mas tarde"
    
    return HttpResponse(respuesta)

def obtenerComentario(request):
    idComentario = request.POST.get('json_name')
    idComentario = int(idComentario)
    comentario = models_comentarios.Comentarios.objects.get(id=idComentario).contenido
    return HttpResponse(comentario)