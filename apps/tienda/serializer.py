from rest_framework import serializers
from apps.tienda.models import Tienda
from apps.libro.models import Libro
from apps.usuarios.models import Usuario

class LibroSerializer(serializers.ModelSerializer):
    autor = serializers.CharField(source='autor.nombre')  # Incluye el nombre del autor
    fecha_creacion = serializers.DateTimeField(format='%Y-%m-%d')  # Formato de fecha
    fecha_actualizacion = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'autor']

class TiendaSerializer(serializers.ModelSerializer):
    libros = LibroSerializer(many=True, read_only=True)  # Incluye los libros relacionados

    class Meta:
        model = Tienda
        fields = ['id', 'nombre', 'ubicacion', 'telefono', 'libros']

class UsuarioSerializer(serializers.ModelSerializer):
    tiendas = TiendaSerializer(many=True, read_only=True)  # Incluye las tiendas relacionadas

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'tiendas']
