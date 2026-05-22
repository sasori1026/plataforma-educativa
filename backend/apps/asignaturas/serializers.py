from rest_framework import serializers
from .models import Asignatura
from apps.usuarios.serializers import UsuarioListSerializer

class AsignaturaSerializer(serializers.ModelSerializer):
    profesor = UsuarioListSerializer(read_only=True)
    profesor_id = serializers.PrimaryKeyRelatedField(source='profesor', queryset=None, write_only=True, allow_null=True)
    class Meta:
        model = Asignatura
        fields = [
            'id', 'codigo', 'nombre', 'descripcion', 'profesor', 'profesor_id', 'creditos', 'semestre',
            'estado', 'fecha_inicio', 'fecha_fin', 'tematica', 'porcentaje_completado', 'fecha_creacion', 'fecha_actualizacion',
        ]
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion', 'profesor')
