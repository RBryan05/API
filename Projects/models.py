from django.db import models

# Create your models here.

class Jugadores(models.Model):
    Nombre = models.CharField(max_length=15, null=False, blank=False)
    Puntaje = models.CharField(max_length=10, null=False, blank=False)
    ModoDeJuego = models.CharField(max_length=30, null=False, blank=False)
