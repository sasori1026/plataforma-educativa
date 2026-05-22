from django.db import models
from apps.modulos.models import Modulo
from apps.usuarios.models import Usuario

class Archivo(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='archivos')
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    descripcion = models.TextField(blank=True)
    subido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    publico = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['-fecha_subida']
    def __str__(self):
        return f"{self.nombre} ({self.modulo})"
