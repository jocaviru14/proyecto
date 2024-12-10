# apps/tu_app/serializers.py

from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'nombres', 'apellidos', 'telefono', 'usuario_activo', 'usuario_administrador')
