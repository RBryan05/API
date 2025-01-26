from .models import Preguntas
from rest_framework import viewsets, permissions
from .serializers import PreguntasSerializer

class PreguntasViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PreguntasSerializer