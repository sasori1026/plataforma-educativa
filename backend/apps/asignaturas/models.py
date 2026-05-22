from django.db import models
from apps.usuarios.models import Usuario

class Asignatura(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('archivada', 'Archivada'),
        ('planificacion', 'En planificación'),
    ]
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="asignaturas")
    creditos = models.PositiveSmallIntegerField(default=3)
    semestre = models.PositiveSmallIntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activa')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tematica = models.CharField(max_length=100, blank=True)
    porcentaje_completado = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['nombre']
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
