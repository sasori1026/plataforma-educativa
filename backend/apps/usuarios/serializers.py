from rest_framework import serializers
from .models import Usuario, AuditLog

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Usuario
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'rol',
            'numero_documento', 'telefono', 'avatar', 'biografia',
            'password', 'confirm_password', 'activo', 'fecha_creacion'
        )
        read_only_fields = ('id', 'fecha_creacion')
    def validate(self, data):
        if 'password' in data:
            if data.get('password') != data.get('confirm_password'):
                raise serializers.ValidationError({'password': 'Las contraseñas no coinciden.'})
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)
        usuario.save()
        return usuario
    def update(self, instance, validated_data):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class UsuarioListSerializer(serializers.ModelSerializer):
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'rol', 'rol_display', 'avatar')

class AuditLogSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.get_full_name', read_only=True)
    accion_display = serializers.CharField(source='get_accion_display', read_only=True)
    class Meta:
        model = AuditLog
        fields = ('id', 'usuario', 'usuario_nombre', 'accion', 'accion_display', 'modelo', 'objeto_id', 'detalles', 'fecha')
        read_only_fields = '__all__'
