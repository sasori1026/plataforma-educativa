from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Usuario, AuditLog
from .serializers import UsuarioSerializer, UsuarioListSerializer, AuditLogSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    filterset_fields = ['rol', 'activo']
    ordering_fields = ['fecha_creacion', 'username']
    ordering = ['-fecha_creacion']
    def get_serializer_class(self):
        if self.action == 'list':
            return UsuarioListSerializer
        return UsuarioSerializer
    def get_permissions(self):
        if self.action in ['register', 'login']:
            return [AllowAny()]
        return super().get_permissions()
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        return Response(
            {'mensaje': 'Usuario registrado exitosamente.', 'usuario': UsuarioListSerializer(usuario).data},
            status=status.HTTP_201_CREATED
        )
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Usuario y contraseña son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)
        usuario = authenticate(username=username, password=password)
        if not usuario:
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'usuario': UsuarioListSerializer(usuario).data,
        })
    @action(detail=False, methods=['get'])
    def perfil(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    @action(detail=False, methods=['put'])
    def cambiar_contraseña(self, request):
        usuario = request.user
        contraseña_actual = request.data.get('contraseña_actual')
        contraseña_nueva = request.data.get('contraseña_nueva')
        confirmar_contraseña = request.data.get('confirmar_contraseña')
        if not usuario.check_password(contraseña_actual):
            return Response({'error': 'Contraseña actual incorrecta.'}, status=status.HTTP_400_BAD_REQUEST)
        if contraseña_nueva != confirmar_contraseña:
            return Response({'error': 'Las contraseñas nuevas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)
        usuario.set_password(contraseña_nueva)
        usuario.save()
        return Response({'mensaje': 'Contraseña actualizada exitosamente.'})

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['usuario', 'accion', 'modelo']
    ordering = ['-fecha']
    def get_queryset(self):
        if self.request.user.es_administrador():
            return AuditLog.objects.all()
        return AuditLog.objects.filter(usuario=self.request.user)
