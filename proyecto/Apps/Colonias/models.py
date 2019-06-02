from django.db import models

# Create your models here.
class Colonias(models.Model):
    nombre = models.CharField(max_length=50)
    codigopostal = models.IntegerField(5)
    referencias = models.CharField(max_length=90)

