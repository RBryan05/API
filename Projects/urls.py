from rest_framework import routers
from Projects.api import JugadoresViewSet

router = routers.DefaultRouter()

router.register('api/jugadores', JugadoresViewSet, 'jugadores')

urlpatterns = router.urls