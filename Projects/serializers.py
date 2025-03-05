from rest_framework import serializers
from .models import Jugadores

class JugadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id', 'Nombre', 'Puntaje')