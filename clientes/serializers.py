from django.forms import widgets
from rest_framework import serializers
from clientes.models import Cliente


class ClienteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    identificacion = serializers.CharField(required=True)
    nombres = serializers.CharField(required=False)
    apellidos = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Cliente` instance, given the validated data.
        """
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.identificacion = validated_data.get('idetificacion', instance.identificacion)
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.save()
        return instance