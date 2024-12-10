from django.db import models

from apps.tienda.models import Tienda
class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50) 
    edad = models.IntegerField(verbose_name="Edad")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50, null=True)
    tiene_premio_nobel = models.BooleanField(verbose_name="Tiene premio nobel?", default=False)

    class Meta:
        verbose_name = "Autor"

    def __str__(self):
        return self.nombre
    
    
class Libro(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(verbose_name="Fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Libro"

    def __str__(self):
        return self.nombre
