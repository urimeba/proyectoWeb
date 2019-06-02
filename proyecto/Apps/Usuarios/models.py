from django.db import models
from django.contrib.auth.models import User
from Apps.Colonias import models as models_colonias
from django.contrib.auth import get_user_model

# Create your models here.
class Usuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    colonia = models.ForeignKey(models_colonias.Colonias, on_delete=models.CASCADE)
