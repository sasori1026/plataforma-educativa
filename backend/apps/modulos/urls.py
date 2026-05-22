from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModuloViewSet, SubModuloViewSet, ActividadViewSet, TareaViewSet, EntregaViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'submodulos', SubModuloViewSet, basename='submodulo')
router.register(r'actividades', ActividadViewSet, basename='actividad')
router.register(r'tareas', TareaViewSet, basename='tarea')
router.register(r'entregas', EntregaViewSet, basename='entrega')

urlpatterns = [
    path('', include(router.urls)),
]
