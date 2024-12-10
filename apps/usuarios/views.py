from django.shortcuts import render
# apps/tu_app/views.py

from rest_framework import generics
from rest_framework import viewsets
from apps.usuarios.models import Usuario
from apps.usuarios.serializer import UsuarioSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.prefetch_related('tiendas__libro_set')  # Optimiza consultas para tiendas y libros
    serializer_class = UsuarioSerializer
