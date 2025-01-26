from rest_framework import routers
from Projects.api import PreguntasViewSet

router = routers.DefaultRouter()

router.register('api/preguntas', PreguntasViewSet, 'preguntas')

urlpatterns = router.urls