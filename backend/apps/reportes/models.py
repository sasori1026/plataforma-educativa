from django.db import models
from apps.usuarios.models import Usuario
from backend.apps.asignaturas.models import Asignatura

class Reporte(models.Model):
    TIPO_CHOICES = [
        ('progreso','Progreso'),
        ('incidencia','Incidencia'),
        ('comentario','Comentario'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reportes')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField()
    detalle = models.JSONField(default=dict, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['-fecha_creacion']
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.usuario} - {self.fecha_creacion}"