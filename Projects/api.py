from .models import Jugadores
from rest_framework import viewsets, permissions
from .serializers import JugadoresSerializer

class JugadoresViewSet(viewsets.ModelViewSet):
    queryset = Jugadores.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JugadoresSerializer