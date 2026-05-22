from rest_framework import viewsets, permissions
from .models import Archivo
from .serializers import ArchivoSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['modulo', 'publico', 'subido_por']
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['fecha_subida', 'nombre']
    ordering = ['-fecha_subida']
