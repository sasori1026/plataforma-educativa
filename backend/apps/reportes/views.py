from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reporte
from .serializers import ReporteSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['tipo','usuario','asignatura']
    ordering = ['-fecha_creacion']
    search_fields = ['descripcion','detalle']
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
