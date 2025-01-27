from rest_framework import serializers
from .models import Preguntas

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ('id', 'pregunta', 'respuesta', 'opcion1', 'opcion2', 'opcion3', 'preguntaImagen', 'materia')

    def get_preguntaImagen(self, obj):
        request = self.context.get('request')  # Obtén el contexto de la solicitud
        if obj.preguntaImagen:
            return request.build_absolute_uri(obj.preguntaImagen.url)  # Devuelve la URL completa
        return None