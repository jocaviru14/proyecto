from rest_framework import serializers
from apps.libro.models import Libro
from apps.libro.models import Autor
from apps.tienda.serializer import TiendaSerializer
from apps.tienda.models import Tienda

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre']

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    tienda = TiendaSerializer()
    fecha_creacion = serializers.SerializerMethodField()
    fecha_actualizacion = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'autor', 'tienda']
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']

    def get_fecha_creacion(self, obj):
        return obj.fecha_creacion.strftime('%d/%m/%Y - %H:%M:%S')

    def get_fecha_actualizacion(self, obj):
        return obj.fecha_actualizacion.strftime('%d/%m/%Y - %H:%M:%S')

    def create(self, validated_data):
        autor_nombre = validated_data.pop('autor')
        autor, created = Autor.objects.get_or_create(
            nombre=autor_nombre,
            defaults={'edad': 30}  # Puedes ajustar el valor por defecto según tus necesidades
        )

        tienda_nombre = validated_data.pop('tienda')
        tienda, created = Tienda.objects.get_or_create(nombre=tienda_nombre)

        libro = Libro.objects.create(autor=autor, tienda=tienda, **validated_data)
        return libro




