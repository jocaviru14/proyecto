from django.contrib import admin
from .models import Tienda
from apps.libro.models import Libro  # Si el modelo Libro está relacionado con Tienda
from apps.usuarios.models import Usuario  # Importa el modelo Usuario para autocomplete

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "telefono", "propietario", "libros_asociados")
    list_filter = ("propietario",)  # Filtrar por propietario
    search_fields = ("nombre", "ubicacion", "telefono", "propietario__username")  # Buscar por nombre de usuario
    autocomplete_fields = ["propietario"]  # Activar autocompletar para el propietario

    def libros_asociados(self, obj):
        # Listar los libros relacionados con la tienda
        libros = Libro.objects.filter(tienda=obj)
        return ", ".join([libro.nombre for libro in libros])

    libros_asociados.short_description = "Libros en esta tienda"
