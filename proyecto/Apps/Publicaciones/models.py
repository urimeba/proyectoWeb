from django.db import models
from Apps.Usuarios import models as models_usuarios
from Apps.Colonias import models as models_colonias
from Apps.Categorias import models as models_categorias
from Apps.Comentarios import models as models_comentarios

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=600)
    usuario = models.ForeignKey(models_usuarios.Usuarios, on_delete=models.CASCADE)
    colonia = models.ForeignKey(models_colonias.Colonias, on_delete=models.CASCADE)
    categoria = models.ForeignKey(models_categorias.Categorias, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        ordering=('-fecha',)


