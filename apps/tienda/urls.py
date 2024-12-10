from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tienda.views import TiendaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'tiendas', TiendaViewSet, basename='tiendas')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')  # Nuevo endpoint para usuarios

urlpatterns = [
    path('api/', include(router.urls)),
]