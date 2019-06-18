from django.db import models
from django.contrib.auth.models import User
from Apps.Usuarios import models as models_usuarios
from Apps.Publicaciones import models as models_publicaciones
from django.conf import settings

# Create your models here.
class Comentarios(models.Model):
    contenido = models.CharField(max_length=200)
    usuario = models.ForeignKey(models_usuarios.Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

class comentarios_publicaciones(models.Model):
    publicacion = models.ForeignKey(models_publicaciones.Publicaciones, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
