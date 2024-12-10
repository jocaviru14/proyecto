from django.db import models
from apps.usuarios.models import Usuario  # Importar el modelo Usuario de la app usuarios

class Tienda(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)
    ubicacion = models.CharField(verbose_name='Dirección', max_length=50)
    telefono = models.CharField(verbose_name='Número de Teléfono', max_length=7)
    propietario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='tiendas',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Tienda"

    def __str__(self):
        return self.nombre
