from django.db import models

# Create your models here.

class Preguntas(models.Model):
    pregunta = models.CharField(max_length=5000, null=True, blank=True)
    respuesta = models.CharField(max_length=5000, null=True, blank=True)
    opcion1 = models.CharField(max_length=5000, null=True, blank=True)
    opcion2 = models.CharField(max_length=5000, null=True, blank=True)
    opcion3 = models.CharField(max_length=5000, null=True, blank=True)
    preguntaImagen = models.ImageField(max_length=5000, null=True, blank=True)
    materia = models.CharField(max_length=5000, null=True, blank=True)
