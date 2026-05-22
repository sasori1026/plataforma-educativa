from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Asignatura
from .serializers import AsignaturaSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['estado', 'semestre', 'profesor']
    search_fields = ['codigo', 'nombre', 'descripcion', 'tematica']
    ordering_fields = ['nombre', 'fecha_creacion', 'fecha_inicio']
    ordering = ['nombre']

    def perform_create(self, serializer):
        # Asignar el usuario actual como profesor si no se indica otro
        if not serializer.validated_data.get('profesor'):
            serializer.save(profesor=self.request.user)
        else:
            serializer.save()
