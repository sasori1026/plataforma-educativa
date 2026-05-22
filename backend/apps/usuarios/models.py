from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class Usuario(AbstractUser):
    """Modelo extendido de Usuario con roles y metadata adicional."""
    ROLES = (
        ('administrador', 'Administrador'),
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')
    numero_documento = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    biografia = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_rol_display()})"

    def es_administrador(self):
        return self.rol == 'administrador'

    def es_profesor(self):
        return self.rol == 'profesor'

    def es_estudiante(self):
        return self.rol == 'estudiante'

class AuditLog(models.Model):
    """Registro de auditoría de cambios en el sistema."""
    ACCIONES = (
        ('crear', 'Crear'),
        ('actualizar', 'Actualizar'),
        ('eliminar', 'Eliminar'),
        ('descargar', 'Descargar'),
        ('subir', 'Subir'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=20, choices=ACCIONES)
    modelo = models.CharField(max_length=100)
    objeto_id = models.IntegerField()
    detalles = models.JSONField(default=dict, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        verbose_name = 'Registro de Auditoría'
        verbose_name_plural = 'Registros de Auditoría'
        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['usuario', '-fecha']),
            models.Index(fields=['modelo', 'objeto_id']),
        ]
    def __str__(self):
        return f"{self.usuario} - {self.get_accion_display()} - {self.modelo}"
