from rest_framework import viewsets
from apps.usuarios.models import Usuario
from apps.usuarios.serializer import UsuarioSerializer

# Vista para los usuarios y sus tiendas con libros
class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.prefetch_related('tiendas__libro_set')  # Optimiza consultas para tiendas y libros
    serializer_class = UsuarioSerializer
