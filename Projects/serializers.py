from rest_framework import serializers
from .models import Preguntas

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('id', 'pregunta', 'respuesta', 'opcion1', 'opcion2', 'opcion3', 'preguntaImagen', 'materia')