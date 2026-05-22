from rest_framework import viewsets, permissions
from .models import Modulo, SubModulo, Actividad, Tarea, Entrega
from .serializers import ModuloSerializer, SubModuloSerializer, ActividadSerializer, TareaSerializer, EntregaSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['asignatura']
    search_fields = ['nombre', 'descripcion']

class SubModuloViewSet(viewsets.ModelViewSet):
    queryset = SubModulo.objects.all()
    serializer_class = SubModuloSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['modulo']
    search_fields = ['nombre', 'descripcion']

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['submodulo', 'tipo']
    search_fields = ['nombre', 'descripcion']

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['actividad', 'activa']
    search_fields = ['titulo', 'descripcion']

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['tarea', 'estudiante']
