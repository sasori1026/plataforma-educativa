from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet

router = DefaultRouter()
router.register(r'', AsignaturaViewSet, basename='asignatura')

urlpatterns = [
    path('', include(router.urls)),
]
