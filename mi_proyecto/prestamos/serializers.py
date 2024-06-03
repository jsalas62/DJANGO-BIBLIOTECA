from rest_framework import serializers
from .models import Prestamo, Libro, Usuario, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()

    class Meta:
        model = Libro
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PrestamoSerializer(serializers.ModelSerializer):
    libro = serializers.PrimaryKeyRelatedField(queryset=Libro.objects.all())
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Prestamo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['libro'] = LibroSerializer(instance.libro).data
        representation['usuario'] = UsuarioSerializer(instance.usuario).data
        return representation
