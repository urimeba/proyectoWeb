from django.shortcuts import render, HttpResponse
import json
from Apps.Comentarios import models as models_comentarios
from Apps.Usuarios import models as models_usuarios

# Create your views here.
def publicarComentario(request):
    datos = request.POST.get('json_name')
    datos = json.loads(datos)

    contenido = datos['comentario']
    publicacion= int(datos['id'])
    usuario = request.user.id
    usuario_usuario = models_usuarios.Usuarios.objects.get(usuario_id=usuario)

    try:
        comentario = models_comentarios.Comentarios(contenido=contenido, usuario=usuario_usuario)
        comentario.save()

        comentario_comentario = models_comentarios.comentarios_publicaciones(comentario_id=comentario.id, publicacion_id=publicacion)
        comentario_comentario.save()
    except Exception as e:
        print(e)
  
    return HttpResponse("Hola")

def eliminarComentario(request,pk):
    print(pk)
    comentario = models_comentarios.Comentarios.objects.get(id=pk)
    comentario.delete()
    return HttpResponse("Hola")
