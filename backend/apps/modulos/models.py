from django.db import models
from apps.asignaturas.models import Asignatura

class Modulo(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='modulos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=1)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    porcentaje_completado = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['orden','nombre']
    def __str__(self):
        return f"{self.asignatura.codigo} - {self.nombre}"

class SubModulo(models.Model):
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE, related_name='submodulos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=1)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = 'Submódulo'
        verbose_name_plural = 'Submódulos'
        ordering = ['orden','nombre']
    def __str__(self):
        return f"{self.modulo} - {self.nombre}"

class Actividad(models.Model):
    submodulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE, related_name='actividades')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=50, default='actividad')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['fecha_inicio','nombre']
    def __str__(self):
        return f"{self.submodulo} - {self.nombre}"

class Tarea(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_entrega = models.DateTimeField()
    puntaje_maximo = models.DecimalField(default=10.0, max_digits=5, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['fecha_entrega']
    def __str__(self):
        return f"{self.actividad} - {self.titulo}"

class Entrega(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='entregas')
    estudiante = models.ForeignKey('apps.usuarios.Usuario', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='entregas/')
    comentario = models.TextField(blank=True)
    puntaje = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retroalimentacion = models.TextField(blank=True)
    entregado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
        unique_together = ('tarea', 'estudiante')
        ordering = ['-entregado_en']
    def __str__(self):
        return f"{self.tarea} - {self.estudiante}"