from django.db import models
from Apps.Colonias import models as models_colonias

# Create your models here.
class Categorias(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=50)