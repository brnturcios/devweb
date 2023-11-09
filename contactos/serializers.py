from rest_framework import serializers
from .models import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ('id', 'nombre', 'direccion', 'telefono', 'create_at')
        read_only_fields = ('create_at', )