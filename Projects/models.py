from django.db import models

# Create your models here.

class Preguntas(models.Model):
    pregunta = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=100)
    opcion1 = models.CharField(max_length=100)
    opcion2 = models.CharField(max_length=100)
    opcion3 = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='preguntas', null=True, blank=True)
    materia = models.CharField(max_length=100)
