from django.contrib import admin
from apps.libro.models import Libro, Autor 

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "autor", "tienda", "fecha_creacion", "fecha_actualizacion")

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "nacionalidad", "tiene_premio_nobel")


#admin.site.register(Libro)
#admin.site.register(Autor)